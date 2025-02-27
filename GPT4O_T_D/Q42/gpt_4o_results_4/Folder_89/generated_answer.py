def prime_factors(numbers):

    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    def get_prime_factors(n):
        primes = set()
        while n % 2 == 0:
            primes.add(2)
            n //= 2
        for i in range(3, int(n ** 0.5) + 1, 2):
            while n % i == 0:
                if is_prime(i):
                    primes.add(i)
                n //= i
        if n > 2:
            primes.add(n)
        return primes
    if not 0 <= 18 < len(numbers):
        return set()
    return get_prime_factors(numbers[18])