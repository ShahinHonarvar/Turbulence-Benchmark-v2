def find_smallest_num(numbers):
    if len(numbers) < 64:
        raise ValueError('List must contain at least 64 numbers.')
    return min(numbers[22:64])