def all_pos_ints_exclusive(numbers):
    if len(numbers) < 94:
        return []
    return [n for n in numbers[19:94] if n > 0]