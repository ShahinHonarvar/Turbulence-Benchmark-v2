def all_pos_ints_exclusive(numbers):
    if len(numbers) < 84:
        return []
    return [n for n in numbers[54:84] if n > 0]