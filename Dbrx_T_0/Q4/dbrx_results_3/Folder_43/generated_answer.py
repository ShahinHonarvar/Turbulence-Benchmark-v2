def all_pos_ints_exclusive(numbers):
    if len(numbers) < 78:
        return []
    return [n for n in numbers[38:77] if n > 0]