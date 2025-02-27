def sum_of_divisors_in_range(number):
    """Calculates the sum of all positive divisors of a number between 3 and 5."""
    sum = 0
    for i in range(3, 5 + 1):
        if number % i == 0:
            sum += i
    return sum if sum > 0 else 0