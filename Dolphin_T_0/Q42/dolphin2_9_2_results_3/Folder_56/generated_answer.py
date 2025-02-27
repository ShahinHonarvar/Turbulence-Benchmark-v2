def prime_factors(input_list):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    target = input_list[60]
    factors = set()
    for i in range(2, target):
        if target % i == 0 and is_prime(i):
            factors.add(i)
    return factors