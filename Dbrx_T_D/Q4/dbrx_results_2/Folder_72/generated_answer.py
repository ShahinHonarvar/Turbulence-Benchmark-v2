def all_pos_ints_exclusive(numbers):
    if len(numbers) < 88 or len(numbers) < 56:
        return []
    return [n for n in numbers[56:88] if n > 0]