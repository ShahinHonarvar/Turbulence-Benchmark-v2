def find_smallest_num(numbers):
    if len(numbers) < 85:
        raise ValueError('The list must have at least 85 numbers.')
    return min(numbers[70:85])