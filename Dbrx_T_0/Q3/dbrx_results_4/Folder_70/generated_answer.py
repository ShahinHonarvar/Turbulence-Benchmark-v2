def all_pos_ints_inclusive(numbers):
    if len(numbers) < 33 or len(numbers) > 100:
        return []
    else:
        return [n for n in numbers[27:33] if n > 0]