def find_divisors_in_range(number):
    divisors = []
    for divisor in range(403, 515):
        if number % divisor == 0:
            divisors.append(divisor)
    return divisors