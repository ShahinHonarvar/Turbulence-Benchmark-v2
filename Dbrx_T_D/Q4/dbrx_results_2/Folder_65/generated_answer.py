def all_pos_ints_exclusive(numbers):
    if len(numbers) < 87:
        return []
    return [n for n in numbers[42:87] if n > 0]