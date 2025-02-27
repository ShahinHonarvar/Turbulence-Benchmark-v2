def prime_factors(numbers):
    number = numbers[38]
    prime_factors_set = set()
    i = 2
    while i * i <= number:
        if number % i:
            i += 1
        else:
            number //= i
            prime_factors_set.add(i)
    if number > 1:
        prime_factors_set.add(number)
    return prime_factors_set