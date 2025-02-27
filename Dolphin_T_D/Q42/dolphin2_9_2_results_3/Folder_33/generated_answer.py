def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    factors = []
    for i in range(2, numbers[321] + 1):
        if is_prime(i):
            while numbers[321] % i == 0:
                factors.append(i)
                numbers[321] //= i
    return set(factors)