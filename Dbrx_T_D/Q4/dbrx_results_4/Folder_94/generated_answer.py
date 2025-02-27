def all_pos_ints_exclusive(numbers):
    if len(numbers) < 53 or 28 > len(numbers):
        return []
    return [n for n in numbers[28:53] if n > 0]