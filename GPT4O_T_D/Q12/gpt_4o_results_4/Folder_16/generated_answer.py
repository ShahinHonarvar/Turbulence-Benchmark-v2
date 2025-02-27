def find_smallest_num(numbers):
    if len(numbers) < 75:
        return None
    return min(numbers[26:75])