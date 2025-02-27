def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def factors(n):
        result = set()
        for i in range(2, n):
            while n % i == 0:
                result.add(i)
                n //= i
            if is_prime(n):
                result.add(n)
                break
        return result
    if len(numbers) > 632:
        return factors(numbers[632])
    return set()