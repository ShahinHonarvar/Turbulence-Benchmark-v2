def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def factors(n):
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
        return {i} if n > 1 else set()
    if len(numbers) > 100:
        number = numbers[100]
        prime_factors_set = set()
        for i in range(2, number + 1):
            while number % i == 0 and is_prime(i):
                prime_factors_set.add(i)
                number //= i
        return prime_factors_set
    return set()