def find_largest_num(numbers):
    if len(numbers) < 21:
        return None
    return max(numbers[20:201])