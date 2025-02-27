def all_pos_ints_inclusive(numbers):
    if len(numbers) < 72:
        return []
    return [n for n in numbers[30:73] if n > 0]