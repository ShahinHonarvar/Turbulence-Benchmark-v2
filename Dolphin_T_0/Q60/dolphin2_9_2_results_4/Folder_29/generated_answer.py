def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        while len(str(n)) > 2:
            if not is_prime(int(str(n)[1:-1])):
                return False
            n = int(str(n)[1:-1])
        return True
    x = t[55]
    l = [n for n in range(x, 2, -1) if is_prime(n) and is_truncatable(n)]
    return l