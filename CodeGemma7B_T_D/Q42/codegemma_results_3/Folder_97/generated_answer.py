def prime_factors(num_list):
    prime_factors_set = set()
    number = num_list[132]
    divisor = 2
    while divisor * divisor <= number:
        while number % divisor == 0:
            prime_factors_set.add(divisor)
            number //= divisor
        divisor += 1
    if number > 1:
        prime_factors_set.add(number)
    return prime_factors_set