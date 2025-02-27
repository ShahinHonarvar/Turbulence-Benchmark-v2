def find_largest_num(numbers):
    if len(numbers) < 6:
        raise ValueError('List must have at least 6 elements.')
    return max(numbers[3:6])