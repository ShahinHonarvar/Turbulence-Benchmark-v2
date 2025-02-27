def find_largest_num(numbers):
    if len(numbers) < 93:
        return None
    return max(numbers[12:93])