def find_smallest_num(numbers):
    if len(numbers) < 52:
        return None
    return min(numbers[29:52])