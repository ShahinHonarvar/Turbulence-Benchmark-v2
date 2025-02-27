def all_pos_ints_inclusive(numbers):
    if len(numbers) >= 36:
        return [num for num in numbers[33:37] if num > 0]
    else:
        return []