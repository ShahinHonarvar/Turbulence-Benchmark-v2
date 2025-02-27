def find_largest_num(numbers):
    if len(numbers) >= 36:
        return max(numbers[32:36])
    return None