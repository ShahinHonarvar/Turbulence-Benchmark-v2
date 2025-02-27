def all_left_truncatable_prime(t):

    def is_truncatable_prime(n):
        if n < 2:
            return False
        str_n = str(n)
        if '0' in str_n:
            return False
        while str_n:
            if not is_prime(int(str_n)):
                return False
            str_n = str_n[1:]
        return True

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[760]
    return [i for i in range(x, 1, -1) if is_truncatable_prime(i)]