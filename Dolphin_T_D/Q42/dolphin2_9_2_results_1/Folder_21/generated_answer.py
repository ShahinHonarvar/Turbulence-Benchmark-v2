def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    prime_factors_set = set()
    for i in range(2, numbers[410] + 1):
        if is_prime(i) and numbers[410] % i == 0:
            prime_factors_set.add(i)
    return prime_factors_set