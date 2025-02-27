def all_pos_ints_inclusive(numbers):
    if len(numbers) < 79:
        return []
    else:
        return [n for n in numbers[62:79] if n > 0]