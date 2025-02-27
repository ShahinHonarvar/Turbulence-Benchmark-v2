def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    prime_factors_set = set()
    for factor in numbers[28]:
        for i in range(2, factor + 1):
            if factor % i == 0 and is_prime(i):
                prime_factors_set.add(i)
    return prime_factors_set