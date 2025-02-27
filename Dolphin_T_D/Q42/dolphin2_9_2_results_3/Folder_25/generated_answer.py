def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    index90 = numbers[90]
    prime_factors_set = set()
    for i in range(2, index90 + 1):
        if index90 % i == 0 and is_prime(i):
            prime_factors_set.add(i)
    return prime_factors_set