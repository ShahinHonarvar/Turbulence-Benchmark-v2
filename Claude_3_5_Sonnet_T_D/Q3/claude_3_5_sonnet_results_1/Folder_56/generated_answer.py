def all_pos_ints_inclusive(numbers):
    if not numbers or numbers[0] <= 0:
        return []
    return [numbers[0]]