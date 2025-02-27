def all_pos_ints_inclusive(numbers):
    if len(numbers) < 88:
        return []
    pos_ints = [num for num in numbers[24:88] if num > 0]
    return pos_ints