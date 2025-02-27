def find_smallest_num(numbers):
    if len(numbers) < 31:
        return None
    return min(numbers[20:31])