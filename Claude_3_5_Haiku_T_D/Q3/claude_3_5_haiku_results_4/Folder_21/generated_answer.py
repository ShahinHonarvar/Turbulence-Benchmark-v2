def all_pos_ints_inclusive(numbers):
    if len(numbers) <= 975:
        return []
    return [num for num in numbers[639:976] if num > 0]