def all_pos_ints_inclusive(numbers):
    if len(numbers) < 100:
        return []
    return [n for n in numbers[10:101] if n > 0]