def find_largest_num(numbers):
    if len(numbers) < 10:
        return None
    return max(numbers[9:10])