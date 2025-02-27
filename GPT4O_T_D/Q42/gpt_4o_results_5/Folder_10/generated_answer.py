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

    def prime_factors_of_num(num):
        factors = set()
        while num % 2 == 0:
            factors.add(2)
            num //= 2
        for i in range(3, int(num ** 0.5) + 1, 2):
            while num % i == 0:
                if is_prime(i):
                    factors.add(i)
                num //= i
        if num > 2:
            factors.add(num)
        return factors
    if len(numbers) <= 54:
        return set()
    return prime_factors_of_num(numbers[54])