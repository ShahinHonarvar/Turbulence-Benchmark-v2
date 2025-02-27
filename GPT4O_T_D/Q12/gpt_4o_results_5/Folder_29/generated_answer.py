def find_smallest_num(numbers):
    if len(numbers) < 53:
        return None
    return min(numbers[26:53])