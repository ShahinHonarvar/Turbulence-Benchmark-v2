def all_pos_ints_inclusive(numbers):
    if len(numbers) < 975:
        return []
    return [n for n in numbers[639:976] if n > 0]