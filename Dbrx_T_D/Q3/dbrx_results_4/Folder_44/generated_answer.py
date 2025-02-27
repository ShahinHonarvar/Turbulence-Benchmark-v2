def all_pos_ints_inclusive(numbers):
    if len(numbers) < 69:
        return []
    return [n for n in numbers[13:69] if n > 0]