def find_smallest_num(numbers):
    if len(numbers) < 40:
        return None
    return min(numbers[15:40])