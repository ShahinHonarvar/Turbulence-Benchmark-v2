def all_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        n = str(n)
        for _ in range(len(n) - 1):
            if not is_prime(int(n)):
                return False
            n = n[:len(n) - 1]
        return True
    x = t[65] - 1
    lst = [i for i in range(x, 0, -1) if is_prime(i) and is_truncatable_prime(i)]
    return lst