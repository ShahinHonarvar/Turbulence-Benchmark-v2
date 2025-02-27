def find_divisors_in_range(x):
    """Write a function called 'find_divisors_in_range' that takes a positive integer as its argument, and returns the list of all positive divisors of the given integer that are between 6 and 9, both inclusive. If no such divisors exist in the specified range, the function should return an empty list."""
    if x <= 0:
        raise ValueError('Input number must be positive')
    divisors = []
    for i in range(6, 10):
        if x % i == 0:
            divisors.append(i)
    return divisors