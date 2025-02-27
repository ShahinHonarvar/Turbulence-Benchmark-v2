def find_largest_num(numbers):
    if len(numbers) < 40:
        return None
    return max(numbers[15:40])