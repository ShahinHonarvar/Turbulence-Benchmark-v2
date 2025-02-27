def prime_factors(lst):
    factors = set()
    for number in lst:
        for i in range(2, number + 1):
            while number % i == 0:
                factors.add(i)
                number //= i
    return factors