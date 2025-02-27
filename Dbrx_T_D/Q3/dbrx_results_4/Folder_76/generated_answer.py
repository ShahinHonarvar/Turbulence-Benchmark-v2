def all_pos_ints_inclusive(numbers):
    if len(numbers) < 987:
        return []
    return [n for n in numbers[686:988] if n > 0]