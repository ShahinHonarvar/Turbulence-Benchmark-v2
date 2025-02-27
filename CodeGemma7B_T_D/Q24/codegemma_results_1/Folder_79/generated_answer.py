def sum_of_divisors_in_range(n):
    """The function takes a positive integer and returns the sum of all positive divisors of the given integer
    that are between 1 and 8, both inclusive. If no such divisors exist
    in the specified range, the function should return 0."""
    if n <= 0:
        return 0
    sum_div = 0
    for i in range(1, n + 1):
        if n % i == 0:
            if i in range(1, 9):
                sum_div += i
    return sum_div