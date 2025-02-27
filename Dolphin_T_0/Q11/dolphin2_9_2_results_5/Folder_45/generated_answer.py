def find_largest_num(numbers):
    if len(numbers) < 30:
        return None
    return max(numbers[30:31])