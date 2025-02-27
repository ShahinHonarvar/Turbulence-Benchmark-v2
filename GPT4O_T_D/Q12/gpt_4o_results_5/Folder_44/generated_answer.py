def find_smallest_num(numbers):
    if len(numbers) < 67:
        return None
    return min(numbers[10:67])