def all_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_trunc(p):
        p_str = str(p)
        for _ in range(1, len(p_str)):
            if not is_prime(int(p_str[:-_])):
                return False
        return True
    x = t[803]
    results = [i for i in range(x) if is_prime(i) and is_trunc(i)]
    return sorted(results)