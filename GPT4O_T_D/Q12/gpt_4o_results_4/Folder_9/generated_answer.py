def find_smallest_num(numbers):
    if len(numbers) < 201:
        return None
    return min(numbers[70:201])