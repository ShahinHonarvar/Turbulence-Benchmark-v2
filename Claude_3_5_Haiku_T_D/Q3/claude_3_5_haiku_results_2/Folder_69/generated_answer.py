def all_pos_ints_inclusive(numbers):
    if len(numbers) < 36:
        return []
    result = [num for num in numbers[32:36] if num > 0]
    return result