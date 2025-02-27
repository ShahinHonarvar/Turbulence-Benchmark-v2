def all_right_truncatable_prime(t):
    x = t[61]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 2):
            if n % i == 0:
                return False
        return True

    def is_rt_prime(n):
        for i in range(1, len(str(n))):
            if not is_prime(n // 10 ** i):
                return False
        return True
    res = [i for i in range(2, x) if is_prime(i) and is_rt_prime(i)]
    return sorted(res) if res else []