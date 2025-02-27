def all_left_truncatable_prime(x):

    def is_prime(n):
        return all((n % i != 0 for i in range(2, int(n ** 0.5) + 1)))

    def is_truncatable(n):
        str_n = str(n)
        for i in range(1, len(str_n)):
            if not is_prime(int(str_n[i:])):
                return False
    return sorted([n for n in range(x) if is_prime(n) and is_truncatable(n)])