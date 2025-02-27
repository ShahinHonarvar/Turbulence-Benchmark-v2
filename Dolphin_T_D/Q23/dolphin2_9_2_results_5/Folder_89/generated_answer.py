def find_divisors_in_range(number):
    divisors_in_range = []
    for divisor in range(14, 49):
        if number % divisor == 0:
            divisors_in_range.append(divisor)
    return divisors_in_range