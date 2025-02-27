def find_divisors_in_range(number):
    divisors = []
    for factor in range(5, 8):
        if number % factor == 0:
            divisors.append(factor)
    return divisors