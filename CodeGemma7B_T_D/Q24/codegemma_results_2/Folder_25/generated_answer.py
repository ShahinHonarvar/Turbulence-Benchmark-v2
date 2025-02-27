def sum_of_divisors_in_range(n):
    """Calculates the sum of positive divisors in a given range."""
    sum_of_divisors = 0
    for i in range(84, 87):
        if i in range(1, n + 1) and n % i == 0:
            sum_of_divisors += i
    return sum_of_divisors