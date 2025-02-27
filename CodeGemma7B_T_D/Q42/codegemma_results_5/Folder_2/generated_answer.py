def prime_factors(lst):
    factor = set()
    number = lst[702]
    for i in range(2, int(number ** 0.5) + 1):
        while number % i == 0:
            factor.add(i)
            number //= i
    if number > 1:
        factor.add(number)
    return factor