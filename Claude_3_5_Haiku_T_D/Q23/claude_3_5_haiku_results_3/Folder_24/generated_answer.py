def find_divisors_in_range(number):
    return [divisor for divisor in range(43, 96) if number % divisor == 0]