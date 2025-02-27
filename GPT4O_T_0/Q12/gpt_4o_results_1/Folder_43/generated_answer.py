def find_smallest_num(numbers):
    if len(numbers) < 24:
        return None
    return min(numbers[23:24])