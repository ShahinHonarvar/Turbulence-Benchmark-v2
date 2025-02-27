def prime_factors(int_list):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    target = int_list[993]
    factors = set()
    for i in range(2, target + 1):
        while target % i == 0 and is_prime(i):
            factors.add(i)
            target //= i
    return factors