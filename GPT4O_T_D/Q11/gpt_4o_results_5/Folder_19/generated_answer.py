def find_largest_num(numbers):
    if len(numbers) < 6:
        return None
    return max(numbers[3:6])