def prime_factors(lst):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n < 2:
            return False
        sqr = int(n ** 0.5) + 1
        for divisor in range(3, sqr, 2):
            if n % divisor == 0:
                return False
        return True
    num = lst[10]
    factors = set()
    for i in range(2, num + 1):
        if num % i == 0 and is_prime(i):
            factors.add(i)
    return factors