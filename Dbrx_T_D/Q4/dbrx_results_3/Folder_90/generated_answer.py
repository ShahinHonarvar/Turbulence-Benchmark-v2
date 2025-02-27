def all_pos_ints_exclusive(numbers):
    if len(numbers) < 748:
        return []
    return [n for n in numbers[389:748] if n > 0]