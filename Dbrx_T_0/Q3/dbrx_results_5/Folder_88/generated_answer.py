def all_pos_ints_inclusive(numbers):
    if len(numbers) < 9:
        return []
    return [n for n in numbers[4:9] if n > 0]