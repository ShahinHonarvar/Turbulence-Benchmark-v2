def find_divisors_in_range(number):
    divisors = []
    for divisor in range(4, 8):
        if number % divisor == 0:
            divisors.append(divisor)
    return divisors