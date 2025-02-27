def all_pos_ints_inclusive(numbers):
    if len(numbers) < 88:
        return []
    else:
        return [n for n in numbers[29:88] if n > 0]