def prime_factors(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True
    num = numbers[29]
    factors = set()
    i = 2
    while i * i <= num:
        if num % i == 0 and is_prime(i):
            factors.add(i)
            num //= i
        else:
            i += 1
    if num > 1 and is_prime(num):
        factors.add(num)
    return factors