def find_smallest_num(numbers):
    if len(numbers) < 41:
        return None
    return min(numbers[28:41])