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
    n = numbers[0]
    prime_factors_set = set()
    i = 2
    while i <= n:
        if n % i == 0 and is_prime(i):
            prime_factors_set.add(i)
            n //= i
        else:
            i += 1
    return prime_factors_set