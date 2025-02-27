def find_largest_num(numbers):
    if len(numbers) < 52:
        return None
    return max(numbers[29:52])