def find_smallest_num(numbers):
    if len(numbers) < 87:
        raise ValueError('List must contain at least 87 elements')
    return min(numbers[68:87])