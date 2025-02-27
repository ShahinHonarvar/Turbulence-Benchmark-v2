def all_pos_ints_inclusive(numbers):
    if len(numbers) < 86:
        return []
    pos_ints = [num for num in numbers[42:87] if num > 0]
    return pos_ints