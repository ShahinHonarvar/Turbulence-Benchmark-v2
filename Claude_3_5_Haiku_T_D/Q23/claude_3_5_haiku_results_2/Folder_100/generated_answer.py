def find_divisors_in_range(number):
    divisors = []
    for div in range(11, 42):
        if number % div == 0:
            divisors.append(div)
    return divisors