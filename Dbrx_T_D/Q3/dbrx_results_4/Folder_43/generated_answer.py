def all_pos_ints_inclusive(numbers):
    if len(numbers) < 87:
        return []
    else:
        return [n for n in numbers[67:87] if n > 0]