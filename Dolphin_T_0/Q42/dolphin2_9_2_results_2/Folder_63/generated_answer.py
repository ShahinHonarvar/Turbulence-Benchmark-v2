def prime_factors(integer_list):

    def is_prime(n):
        if n in (0, 1):
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return set((i for i in integer_list[57] if is_prime(i)))