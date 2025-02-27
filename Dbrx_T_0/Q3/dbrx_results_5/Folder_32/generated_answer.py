def all_pos_ints_inclusive(numbers):
    if len(numbers) < 98:
        return []
    else:
        return [n for n in numbers[20:98] if n > 0]