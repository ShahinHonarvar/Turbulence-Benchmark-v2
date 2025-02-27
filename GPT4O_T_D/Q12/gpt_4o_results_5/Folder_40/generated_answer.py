def find_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    return min(numbers[0:2])