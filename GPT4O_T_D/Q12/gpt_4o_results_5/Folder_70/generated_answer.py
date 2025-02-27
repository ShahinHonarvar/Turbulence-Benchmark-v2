def find_smallest_num(numbers):
    if len(numbers) < 49:
        return None
    return min(numbers[30:49])