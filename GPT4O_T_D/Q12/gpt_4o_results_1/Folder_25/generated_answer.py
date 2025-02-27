def find_smallest_num(numbers):
    if len(numbers) < 64:
        return None
    return min(numbers[22:64])