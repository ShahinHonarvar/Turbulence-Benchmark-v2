def prime_factors(int_list):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    int_84 = int_list[84]
    factors = set()
    for i in range(1, int_84 + 1):
        if is_prime(i) and int_84 % i == 0:
            factors.add(i)
    return factors