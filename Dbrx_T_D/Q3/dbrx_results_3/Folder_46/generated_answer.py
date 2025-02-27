def all_pos_ints_inclusive(numbers):
    if len(numbers) <= 87 or len(numbers) < 30:
        return []
    else:
        return [n for n in numbers[30:88] if n > 0]