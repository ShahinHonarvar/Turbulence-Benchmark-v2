def all_pos_ints_inclusive(numbers):
    if len(numbers) <= 86:
        return []
    return [num for num in numbers[43:87] if num > 0]