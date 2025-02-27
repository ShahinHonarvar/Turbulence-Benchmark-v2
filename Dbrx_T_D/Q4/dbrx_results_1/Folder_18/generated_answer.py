def all_pos_ints_exclusive(numbers):
    if len(numbers) < 84:
        return []
    elif len(numbers) > 57 and len(numbers) < 84:
        return [n for n in numbers[57:] if isinstance(n, int) and n > 0]
    else:
        return [n for n in numbers[57:84] if isinstance(n, int) and n > 0]