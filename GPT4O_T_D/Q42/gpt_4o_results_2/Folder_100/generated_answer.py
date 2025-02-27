def prime_factors(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_prime_factors(n):
        prime_factors_set = set()
        for i in range(2, n + 1):
            while n % i == 0:
                if is_prime(i):
                    prime_factors_set.add(i)
                n //= i
        return prime_factors_set
    if len(numbers) > 99:
        return get_prime_factors(numbers[99])
    else:
        return set()