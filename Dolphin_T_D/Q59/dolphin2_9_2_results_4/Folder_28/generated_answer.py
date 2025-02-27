def all_left_truncatable_prime(t):
    x = t[19]

    def is_prune(n):
        for p in range(2, int(n ** 0.5) + 1):
            if n % p == 0:
                return False
        return True

    def is_left_truncatable(n):
        num_str = str(n)
        if '0' in num_str:
            return False
        for i in range(1, len(num_str)):
            if not is_prune(int(num_str[i:])):
                return False
        return True
    return [n for n in range(2, x) if is_left_truncatable(n)]