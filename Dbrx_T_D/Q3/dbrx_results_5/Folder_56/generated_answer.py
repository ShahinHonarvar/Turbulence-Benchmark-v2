def all_pos_ints_inclusive(numbers):
    if len(numbers) < 2:
        return []
    return [num for num in numbers if num > 0][:2]