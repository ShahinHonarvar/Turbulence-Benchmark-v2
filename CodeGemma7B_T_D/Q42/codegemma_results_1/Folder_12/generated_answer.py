def prime_factors(lst):
    prime_factors = set()
    for i in range(2, lst[27] + 1):
        if lst[27] % i == 0:
            while lst[27] % i == 0:
                lst[27] //= i
                prime_factors.add(i)
    return prime_factors