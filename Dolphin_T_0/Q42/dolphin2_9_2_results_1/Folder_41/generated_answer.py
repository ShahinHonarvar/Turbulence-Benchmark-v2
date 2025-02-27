def prime_factors(integer_list):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    target_integer = integer_list[84]
    factors = set()
    for i in range(1, target_integer + 1):
        if target_integer % i == 0 and is_prime(i):
            factors.add(i)
    return factors