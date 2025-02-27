def prime_factors(numbers):
    factors = set()
    number = numbers[87]
    i = 2
    while i * i <= number:
        if number % i == 0:
            factors.add(i)
            number //= i
        else:
            i += 1
    if number > 1:
        factors.add(number)
    return factors