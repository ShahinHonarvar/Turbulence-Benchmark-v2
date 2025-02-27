def find_divisors_in_range(number):
    divisors = []
    if number <= 0:
        return divisors
    for val in range(71, 82):
        if number % val == 0:
            divisors.append(val)
    return divisors