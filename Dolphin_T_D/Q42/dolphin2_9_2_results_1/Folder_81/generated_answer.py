def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    factors = set()
    for i in range(2, numbers[20] + 1):
        while numbers[20] % i == 0 and is_prime(i):
            factors.add(i)
            numbers[20] //= i
    return factors