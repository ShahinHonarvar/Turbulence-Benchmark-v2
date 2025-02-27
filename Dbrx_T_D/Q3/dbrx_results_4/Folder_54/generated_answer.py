def all_pos_ints_inclusive(numbers):
    if len(numbers) < 55 or len(numbers) < 34:
        return []
    else:
        return [n for n in numbers[34:56] if n > 0]