def find_largest_num(numbers):
    if len(numbers) < 8:
        return None
    return max(numbers[0:8])