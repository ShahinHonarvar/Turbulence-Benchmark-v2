def prime_factors(lst):

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
    num = lst[93]
    factors = set()
    for i in range(2, int(num ** 0.5) + 1):
        while num % i == 0:
            if is_prime(i):
                factors.add(i)
            num //= i
    if num > 1 and is_prime(num):
        factors.add(num)
    return factors