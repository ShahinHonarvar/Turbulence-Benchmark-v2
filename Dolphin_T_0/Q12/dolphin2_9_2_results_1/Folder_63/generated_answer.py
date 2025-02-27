def find_smallest_num(numbers):
    if len(numbers) < 63:
        return None
    return min(numbers[62:64])