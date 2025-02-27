def prime_factors(integer_list):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    target_integer = integer_list[40]
    prime_factors_set = set()
    for i in range(1, target_integer + 1):
        if target_integer % i == 0 and is_prime(i):
            prime_factors_set.add(i)
    return prime_factors_set