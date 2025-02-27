def all_pos_ints_exclusive(numbers):
    if len(numbers) < 99:
        return []
    return [n for n in numbers[86:99] if n > 0]