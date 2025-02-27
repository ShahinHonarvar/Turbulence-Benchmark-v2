def find_smallest_num(numbers):
    if len(numbers) < 101:
        return None
    return min(numbers[10:101])