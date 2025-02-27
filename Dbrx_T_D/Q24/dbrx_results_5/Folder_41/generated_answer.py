def sum_of_divisors_in_range(num):
    divisors = [divisor for divisor in range(2, 5) if num % divisor == 0]
    return sum(divisors) if divisors else 0