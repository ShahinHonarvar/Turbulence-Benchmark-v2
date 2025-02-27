def all_pos_ints_inclusive(numbers):
    if len(numbers) < 41 or len(numbers) < 28:
        return []
    return [num for num in numbers[28:41] if num > 0]