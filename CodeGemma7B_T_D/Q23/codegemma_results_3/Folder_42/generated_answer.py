def find_divisors_in_range(n):
    """This function returns the list of all positive divisors of the given integer that are between 14 and 93, both inclusive."""
    if n <= 0 or n < 14:
        raise ValueError('Input number must be a positive integer greater than or equal to 14.')
    divisors = []
    for i in range(14, 94):
        if n % i == 0:
            divisors.append(i)
    return divisors or []