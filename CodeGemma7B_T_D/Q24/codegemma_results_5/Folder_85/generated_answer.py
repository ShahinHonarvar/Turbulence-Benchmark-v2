def sum_of_divisors_in_range(number):
    """Calculates the sum of all positive divisors of a number in the range 2 to 5, inclusive."""
    sum_of_divisors = 0
    for divisor in range(2, 6):
        if number % divisor == 0:
            sum_of_divisors += divisor
    return sum_of_divisors