def find_largest_num(numbers):
    if len(numbers) < 87:
        raise ValueError('List must contain at least 87 elements')
    return max(numbers[68:87])