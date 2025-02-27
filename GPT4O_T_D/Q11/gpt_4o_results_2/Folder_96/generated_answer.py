def find_largest_num(numbers):
    if len(numbers) < 201:
        return None
    return max(numbers[50:201])