def find_largest_num(numbers):
    if len(numbers) < 64:
        raise ValueError('The list must contain at least 64 elements.')
    return max(numbers[62:64])