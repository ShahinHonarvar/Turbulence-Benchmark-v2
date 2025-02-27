def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        str_n = str(n)
        for i in range(1, len(str_n)):
            sub_n = int(str_n[i:])
            if not is_prime(sub_n):
                return False
        return True
    x = t[36 - 1]
    return sorted([i for i in range(x - 1, 1, -1) if is_truncatable(i) and is_prime(i)])