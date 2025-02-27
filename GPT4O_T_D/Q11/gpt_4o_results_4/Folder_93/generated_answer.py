def find_largest_num(numbers):
    if len(numbers) < 95:
        return None
    return max(numbers[75:95])