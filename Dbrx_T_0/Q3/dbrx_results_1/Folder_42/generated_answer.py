def all_pos_ints_inclusive(numbers):
    if len(numbers) < 80:
        return []
    return [n for n in numbers[29:80] if n > 0]