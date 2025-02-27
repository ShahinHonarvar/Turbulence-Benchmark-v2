def all_pos_ints_exclusive(numbers):
    if len(numbers) < 43:
        return []
    return [n for n in numbers[20:43] if n > 0]