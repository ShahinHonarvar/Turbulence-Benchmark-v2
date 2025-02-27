def all_pos_ints_inclusive(numbers):
    if len(numbers) < 92:
        return []
    return [n for n in numbers[19:93] if n > 0]