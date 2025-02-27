def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def factors(n):
        factor = 2
        result = []
        while factor * factor <= n:
            if n % factor:
                factor += 1
            else:
                n //= factor
                result.append(factor)
        if n > 1:
            result.append(n)
        return result
    return set(factors(numbers[34]))