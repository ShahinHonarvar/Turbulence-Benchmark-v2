def find_largest_num(numbers):
    if len(numbers) < 86:
        return None
    return max(numbers[75:86])