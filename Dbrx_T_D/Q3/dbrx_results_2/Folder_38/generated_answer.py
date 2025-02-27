def all_pos_ints_inclusive(numbers):
    if len(numbers) < 63:
        return []
    return [n for n in numbers[22:64] if n > 0]