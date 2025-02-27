def prime_factors(lst):
    prime_factors = set()
    for number in lst[43]:
        factor = 2
        while factor * factor <= number:
            if number % factor == 0:
                prime_factors.add(factor)
                number //= factor
            else:
                factor += 1
        if number > 1:
            prime_factors.add(number)
    return prime_factors