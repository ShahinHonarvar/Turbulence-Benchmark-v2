def find_largest_num(numbers):
    if len(numbers) < 63 or len(numbers) > 100:
        raise ValueError('Input list must have between 63 and 100 elements')
    return max(numbers[22:64])