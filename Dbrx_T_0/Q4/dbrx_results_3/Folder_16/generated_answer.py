def all_pos_ints_exclusive(numbers):
    if len(numbers) < 90:
        return []
    return [n for n in numbers[86:90] if n > 0]