def find_divisors_in_range(number):
    divisors = []
    for potential_divisor in range(6, 9):
        if number % potential_divisor == 0:
            divisors.append(potential_divisor)
    return divisors