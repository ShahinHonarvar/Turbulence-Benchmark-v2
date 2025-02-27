def all_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        if len(str(n)) == 1:
            return is_prime(n)
        return is_prime(n) and is_right_truncatable_prime(n / 10)
    x = t[25]
    ret = [i for i in range(x - 1, 0, -1) if is_right_truncatable_prime(i)]
    return ret