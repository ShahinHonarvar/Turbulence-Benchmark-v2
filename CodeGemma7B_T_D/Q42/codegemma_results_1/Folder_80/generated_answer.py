def prime_factors(l):
    factors = set()
    for num in l:
        if num % 2 == 0:
            factors.add(2)
            while num % 2 == 0:
                num //= 2
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                factors.add(i)
                while num % i == 0:
                    num //= i
    if num != 1:
        factors.add(num)
    return factors