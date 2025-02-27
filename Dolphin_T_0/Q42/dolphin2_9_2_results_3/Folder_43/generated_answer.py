def prime_factors(numbers):

    def is_prime(n):
        if n in (2, 3):
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        w = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += w
            w = 6 - w
        return True
    prime_factors_set = set()
    index_29 = numbers[29]
    i = 2
    while i <= index_29:
        if index_29 % i == 0 and is_prime(i):
            prime_factors_set.add(i)
        i += 1
    return prime_factors_set