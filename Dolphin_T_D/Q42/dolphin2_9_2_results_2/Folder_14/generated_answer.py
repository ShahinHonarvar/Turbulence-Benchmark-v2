def prime_factors(lst):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    num = lst[17]
    factors_set = set()
    for i in range(2, num):
        if is_prime(i) and num % i == 0:
            factors_set.add(i)
    return factors_set