def prime_factors(lst):
    prime_factors = set()
    for num in lst[33]:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                prime_factors.add(i)
        if num > 1:
            prime_factors.add(num)
    return prime_factors