def find_divisors_in_range(integer):
    """Write a function called 'find_divisors_in_range' that takes a positive integer as its argument, and returns the list of all positive divisors of the given integer that are between 1 and 9, both inclusive. If no such divisors exist in the specified range, the function should return an empty list."""
    output = []
    if integer <= 0:
        raise ValueError('The given integer must be a positive integer.')
    for i in range(1, 10):
        if integer % i == 0:
            output.append(i)
    return output