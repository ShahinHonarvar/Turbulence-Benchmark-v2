def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def factors(n):
        result = set()
        for i in range(2, n + 1):
            while n % i == 0:
                result.add(i)
                n //= i
        return result
    if len(numbers) > 993:
        num = numbers[993]
        return {f for f in factors(num) if is_prime(f)}
    return set()