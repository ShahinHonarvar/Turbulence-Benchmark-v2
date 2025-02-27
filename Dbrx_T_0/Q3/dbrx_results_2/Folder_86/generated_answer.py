def all_pos_ints_inclusive(numbers):
    if len(numbers) < 35:
        return []
    else:
        return [n for n in numbers[31:35] if n > 0]