def find_largest_num(numbers):
    if len(numbers) < 8:
        return None
    return max(numbers[5:8])