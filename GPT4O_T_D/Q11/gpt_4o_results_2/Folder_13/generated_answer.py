def find_largest_num(numbers):
    if len(numbers) < 88:
        return None
    return max(numbers[25:88])