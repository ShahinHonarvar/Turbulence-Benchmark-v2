def find_largest_num(numbers):
    if len(numbers) <= 200:
        return None
    return max(numbers[40:201])