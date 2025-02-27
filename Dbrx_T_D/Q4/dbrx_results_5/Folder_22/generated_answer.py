def all_pos_ints_exclusive(numbers):
    if len(numbers) < 200:
        return []
    pos_ints = [num for num in numbers[40:200] if num > 0]
    return pos_ints