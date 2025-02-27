def find_largest_num(numbers):
    if len(numbers) < 33:
        return None
    return max(numbers[28:33])