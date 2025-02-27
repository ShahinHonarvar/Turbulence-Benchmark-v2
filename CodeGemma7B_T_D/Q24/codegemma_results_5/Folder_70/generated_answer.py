def sum_of_divisors_in_range(number):
    return sum((divisor for divisor in range(586, 841) if number % divisor == 0)) or 0