def prime_factors(lst):

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    prime_factors = set()
    for factor in lst[38]:
        if is_prime(factor):
            prime_factors.add(factor)
    return prime_factors