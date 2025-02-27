def find_smallest_num(numbers):
    if len(numbers) < 7:
        raise ValueError('The list must contain at least 7 elements.')
    return min(numbers[:7])