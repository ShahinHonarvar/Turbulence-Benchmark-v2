def all_pos_ints_inclusive(numbers):
    if len(numbers) < 55:
        return []
    pos_ints = [num for num in numbers[27:56] if num > 0]
    return pos_ints