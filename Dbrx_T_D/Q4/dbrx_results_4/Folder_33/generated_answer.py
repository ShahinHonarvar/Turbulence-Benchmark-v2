def all_pos_ints_exclusive(numbers):
    if len(numbers) < 983:
        return []
    return [n for n in numbers[369:983] if n > 0]