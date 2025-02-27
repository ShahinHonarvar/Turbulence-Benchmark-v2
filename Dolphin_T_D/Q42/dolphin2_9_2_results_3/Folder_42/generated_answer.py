def prime_factors(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_prime_factors(n):
        prime_factors = []
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                prime_factors.append(i)
        if n > 1:
            prime_factors.append(n)
        return Set(prime_factors)
    return get_prime_factors(numbers[276])