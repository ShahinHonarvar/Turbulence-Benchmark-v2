def find_divisors_in_range(number):
    divisors = []
    if number % 58 == 0:
        divisors.append(58)
    if number % 59 == 0:
        divisors.append(59)
    ...
    if number % 90 == 0:
        divisors.append(90)
    return divisors