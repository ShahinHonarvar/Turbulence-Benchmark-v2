def find_largest_num(numbers):
    if len(numbers) < 31:
        return None
    return max(numbers[30:31])