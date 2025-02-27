def find_smallest_num(numbers):
    if len(numbers) < 100:
        raise ValueError('List must have at least 100 elements.')
    return min(numbers[62:100])