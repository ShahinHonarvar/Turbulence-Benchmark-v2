def all_pos_ints_exclusive(numbers):
    if len(numbers) < 70:
        return []
    else:
        return [n for n in numbers[13:70] if n > 0]