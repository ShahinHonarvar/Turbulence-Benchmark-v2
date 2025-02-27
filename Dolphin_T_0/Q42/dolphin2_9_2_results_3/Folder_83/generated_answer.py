def prime_factors(numbers):

    def is_prime(n):
        if n in (2, 3):
            return True
        if n == 1 or n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    def get_factors(n):
        factors = []
        i = 2
        while n != 1:
            if n % i == 0 and is_prime(i):
                factors.append(i)
                n /= i
            else:
                i += 1
        return factors
    return set(get_factors(numbers[95]))