def all_pos_ints_exclusive(numbers):
    if len(numbers) < 81:
        return []
    else:
        return [n for n in numbers[38:81] if n > 0]