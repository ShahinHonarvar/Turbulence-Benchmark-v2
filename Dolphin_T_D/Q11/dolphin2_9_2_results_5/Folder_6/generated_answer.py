def find_largest_num(numbers):
    if len(numbers) < 66:
        return 'List should have at least 66 elements.'
    return max(numbers[10:67])