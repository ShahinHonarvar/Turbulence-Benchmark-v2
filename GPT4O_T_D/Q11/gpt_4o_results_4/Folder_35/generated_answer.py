def find_largest_num(numbers):
    if len(numbers) < 49:
        return None
    return max(numbers[30:49])