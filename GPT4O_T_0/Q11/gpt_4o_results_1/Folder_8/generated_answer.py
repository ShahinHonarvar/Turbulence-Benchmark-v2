def find_largest_num(numbers):
    if len(numbers) < 24:
        return None
    return max(numbers[23:24])