def find_largest_num(numbers):
    if len(numbers) < 41:
        return None
    return max(numbers[28:41])