def all_pos_ints_inclusive(numbers):
    if len(numbers) >= 36:
        return [n for n in numbers[31:36] if n > 0]
    else:
        return []