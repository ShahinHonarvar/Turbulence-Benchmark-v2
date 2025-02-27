def find_largest_num(numbers):
    if len(numbers) < 2:
        return None
    return max(numbers[0], numbers[1])