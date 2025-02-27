def find_smallest_num(numbers):
    if len(numbers) < 10:
        raise ValueError('List must contain at least 10 elements')
    return min(numbers[8:10])