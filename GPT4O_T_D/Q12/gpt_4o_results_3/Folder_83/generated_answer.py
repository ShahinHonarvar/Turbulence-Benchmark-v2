def find_smallest_num(numbers):
    if len(numbers) >= 201:
        return min(numbers[90:201])
    return None