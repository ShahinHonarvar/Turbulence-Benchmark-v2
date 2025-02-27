def all_pos_ints_inclusive(numbers):
    if len(numbers) <= 23:
        return []
    else:
        return [num for num in numbers[23:24] if num > 0]