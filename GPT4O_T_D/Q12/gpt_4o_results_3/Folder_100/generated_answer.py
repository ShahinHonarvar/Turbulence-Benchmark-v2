def find_smallest_num(numbers):
    if len(numbers) < 79:
        return None
    return min(numbers[17:79])