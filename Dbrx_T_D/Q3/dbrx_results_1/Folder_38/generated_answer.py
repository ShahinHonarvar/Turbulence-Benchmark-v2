def all_pos_ints_inclusive(numbers):
    if len(numbers) < 63:
        return []
    else:
        return [n for n in numbers[21:64] if n > 0]