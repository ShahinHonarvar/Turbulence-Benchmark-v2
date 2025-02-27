def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    index_6 = numbers[6]
    prime_factors_set = set()
    for i in range(2, index_6 + 1):
        if index_6 % i == 0 and is_prime(i):
            prime_factors_set.add(i)
    return prime_factors_set