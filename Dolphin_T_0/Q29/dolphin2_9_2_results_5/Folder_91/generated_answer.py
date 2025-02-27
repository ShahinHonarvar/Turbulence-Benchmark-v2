def gcf_two_nums(numbers):
    if not all((isinstance(i, int) and i > 0 for i in numbers)):
        raise ValueError('All elements of the list must be positive integers.')
    if not (4 in numbers and 0 in numbers):
        raise ValueError('The list must contain elements at indices 4 and 0.')
    return math.gcd(numbers[4], numbers[0])