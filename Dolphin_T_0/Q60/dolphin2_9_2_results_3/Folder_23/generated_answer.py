def all_left_right_truncatable_prime(t):

    def is_prime(n):
        if n == 0 or n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        num = n
        while len(str(n)) > 1:
            n = int(str(n)[1:-1])
            if n < 10 and is_prime(n):
                num = n
        return num
    x = t[77]
    res = [i for i in range(x, 0, -1) if is_prime(i) and i == is_truncatable(i)]
    return res