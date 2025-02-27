def sum_of_divisors_in_range(num):
    """Sums the divisors in a given range."""
    sum_of_divisors = 0
    for i in range(83, 96):
        if num % i == 0:
            sum_of_divisors += i
    return sum_of_divisors