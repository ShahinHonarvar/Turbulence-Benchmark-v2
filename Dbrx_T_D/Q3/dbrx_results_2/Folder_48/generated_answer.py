def all_pos_ints_inclusive(numbers):
    if len(numbers) < 605:
        return []
    return [n for n in numbers[533:606] if n > 0]