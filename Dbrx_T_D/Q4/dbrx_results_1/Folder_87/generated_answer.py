def all_pos_ints_exclusive(numbers):
    if len(numbers) < 99:
        return []
    else:
        return [n for n in numbers[31:99] if n > 0]