def find_smallest_num(numbers):
    if len(numbers) < 7:
        return None
    return min(numbers[6:7])