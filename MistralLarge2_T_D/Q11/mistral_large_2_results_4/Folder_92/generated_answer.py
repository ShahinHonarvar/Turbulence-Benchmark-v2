def find_largest_num(numbers):
    if len(numbers) < 2:
        raise ValueError('List must contain at least two elements')
    return max(numbers[0], numbers[1])