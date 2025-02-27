def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        n_str = str(n)
        return all((is_prime(int(n_str[i:])) for i in range(1, len(n_str))))
    x = t[55]
    return sorted([n for n in range(x, 1, -1) if is_truncatable_prime(n)], reverse=False)