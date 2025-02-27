def find_smallest_num(numbers):
    if len(numbers) < 57 or len(numbers) > 83:
        return None
    return min(numbers[56:83])