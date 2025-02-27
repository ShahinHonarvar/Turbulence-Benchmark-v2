def find_largest_num(numbers):
    if len(numbers) < 31:
        raise IndexError('List must have at least 31 elements')
    return max(numbers[20:31])