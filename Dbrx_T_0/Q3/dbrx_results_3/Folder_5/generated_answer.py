def all_pos_ints_inclusive(numbers):
    if len(numbers) < 10:
        return []
    pos_ints = [num for num in numbers[8:10] if num > 0]
    return pos_ints