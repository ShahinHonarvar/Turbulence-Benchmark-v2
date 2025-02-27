def find_largest_num(numbers):
    if len(numbers) < 36:
        return None
    return max(numbers[32:36])