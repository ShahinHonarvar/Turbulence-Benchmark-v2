def prime_factors(ints):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    int_to_factor = ints[94]
    factors = set()
    for i in range(2, int_to_factor + 1):
        while is_prime(i) and int_to_factor % i == 0:
            factors.add(i)
            int_to_factor //= i
    return factors