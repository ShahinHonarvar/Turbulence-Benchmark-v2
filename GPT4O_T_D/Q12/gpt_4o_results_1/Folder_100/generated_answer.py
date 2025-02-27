def find_smallest_num(numbers):
    if len(numbers) < 79:
        raise ValueError('List must contain at least 79 elements.')
    return min(numbers[17:79])