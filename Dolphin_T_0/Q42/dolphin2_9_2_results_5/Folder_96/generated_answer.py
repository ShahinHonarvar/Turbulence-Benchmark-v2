def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    def prime_factors_of(n):
        result = set()
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                result.add(i)
        if n > 1:
            result.add(n)
        return result
    return prime_factors_of(numbers[47])