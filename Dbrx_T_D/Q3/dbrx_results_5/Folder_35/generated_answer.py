def all_pos_ints_inclusive(numbers):
    if len(numbers) < 48:
        return []
    pos_ints = [num for num in numbers[30:49] if num > 0]
    return pos_ints