def prime_factors(sequence):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def find_prime_factors(num):
        factors = set()
        for i in range(2, num + 1):
            if num % i == 0 and is_prime(i):
                factors.add(i)
                while num % i == 0 and is_prime(num // i):
                    num //= i
        if is_prime(num):
            factors.add(num)
        return factors
    return find_prime_factors(sequence[18])