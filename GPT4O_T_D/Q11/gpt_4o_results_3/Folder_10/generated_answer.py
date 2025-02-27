def find_largest_num(numbers):
    if len(numbers) < 60:
        return None
    return max(numbers[25:60])