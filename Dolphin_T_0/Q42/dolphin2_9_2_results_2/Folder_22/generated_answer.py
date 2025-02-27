def prime_factors(numbers):

    def all_factors(n):
        factors = set()
        for i in range(1, n + 1):
            if n % i == 0:
                factors.add(i)
        return factors

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
    return [all_factors(numbers[72]).intersection(set(filter(is_prime, all_factors(numbers[72]))))]