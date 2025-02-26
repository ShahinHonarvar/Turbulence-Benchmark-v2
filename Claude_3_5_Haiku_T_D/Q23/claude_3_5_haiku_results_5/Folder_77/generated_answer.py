def find_divisors_in_range(number):
    divisors = []
    for divisor in range(111, 509):
        if number % divisor == 0:
            divisors.append(divisor)
    return divisors