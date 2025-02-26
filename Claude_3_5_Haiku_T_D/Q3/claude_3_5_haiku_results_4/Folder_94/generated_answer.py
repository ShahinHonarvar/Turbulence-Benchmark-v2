def all_pos_ints_inclusive(numbers):
    if len(numbers) < 41:
        return []
    pos_ints = [num for num in numbers[28:41] if num > 0]
    return pos_ints