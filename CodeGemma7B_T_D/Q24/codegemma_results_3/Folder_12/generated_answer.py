def sum_of_divisors_in_range(num):
    """Sum of divisors in a range."""
    if num <= 13 or num >= 62:
        return 0
    sum = 0
    for i in range(14, 62):
        if num % i == 0:
            sum += i
    return sum