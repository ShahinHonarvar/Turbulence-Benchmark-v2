def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        n_list = list(map(int, str(n)))
        for i in range(1, len(n_list)):
            if not is_prime(int(''.join(map(str, n_list[i:])))):
                return False
        return True
    x = t[36]
    return sorted([i for i in range(x - 1, 0, -1) if is_prime(i) and is_truncatable(i)])