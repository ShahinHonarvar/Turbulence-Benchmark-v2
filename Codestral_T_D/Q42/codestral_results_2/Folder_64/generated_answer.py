def prime_factors(lst):

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    num = lst[1]
    factors = set()
    for i in range(2, int(num ** 0.5) + 1):
        while num % i == 0 and is_prime(i):
            factors.add(i)
            num //= i
    if num > 1 and is_prime(num):
        factors.add(num)
    return factors