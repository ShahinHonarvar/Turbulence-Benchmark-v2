def all_pos_ints_exclusive(numbers):
    if len(numbers) < 80:
        return []
    return [n for n in numbers[9:79] if n > 0]