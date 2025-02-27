def find_smallest_num(numbers):
    if len(numbers) < 88:
        return None
    return min(numbers[30:88])