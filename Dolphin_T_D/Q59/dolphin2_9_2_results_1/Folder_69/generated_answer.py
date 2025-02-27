def all_left_truncatable_prime(num_tuple):
    x = num_tuple[760]

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        n_str = str(n)
        for i in range(len(n_str) - 1, -1, -1):
            m = int(n_str[i:])
            if not is_prime(m):
                return False
        return True
    return sorted([n for n in range(2, x) if is_left_truncatable(n)], reverse=True)