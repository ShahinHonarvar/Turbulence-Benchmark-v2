def all_pos_ints_inclusive(numbers):
    if len(numbers) < 99:
        return []
    else:
        return [n for n in numbers[54:99] if n > 0]