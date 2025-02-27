def sum_of_divisors_in_range(num):
    return sum((divisor for divisor in range(50, 85) if num % divisor == 0))