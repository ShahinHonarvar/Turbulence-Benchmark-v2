def prime_factors(numbers):

    def is_prime(n):
        if n == 2:
            return True
        if n % 2 == 0 or n == 1:
            return False
        i = 3
        while i * i <= n:
            if n % i:
                i += 2
            else:
                return False
        return True

    def prime_factors_of_n(n):
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
    return prime_factors_of_n(numbers[10]) if is_prime(numbers[10]) else set()