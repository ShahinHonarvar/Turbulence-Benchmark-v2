def find_smallest_num(numbers):
    if len(numbers) < 8:
        return None
    return min(numbers[5:8])