def prime_factors(lst):

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
        factors = set()
        while n % 2 == 0:
            factors.add(2)
            n //= 2
        while n % 3 == 0:
            factors.add(3)
            n //= 3
        i = 5
        while i * i <= n:
            while n % i == 0:
                factors.add(i)
                n //= i
            while n % (i + 2) == 0:
                factors.add(i + 2)
                n //= i + 2
            i += 6
        if n > 1:
            factors.add(n)
        return factors
    if len(lst) <= 35:
        return set()
    number = lst[35]
    return get_prime_factors(number)