def all_pos_ints_exclusive(numbers):
    if len(numbers) < 51:
        return []
    else:
        return [n for n in numbers[20:51] if n > 0]