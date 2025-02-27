def prime_factors(numbers):

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_prime_factors(n):
        factors = []
        i = 2
        while i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        return factors
    return set(get_prime_factors(numbers[459]))