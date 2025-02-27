def all_pos_ints_exclusive(numbers):
    if len(numbers) < 25:
        return []
    pos_ints = [num for num in numbers[21:24] if num > 0]
    return pos_ints