def all_pos_ints_inclusive(numbers):
    if len(numbers) >= 39:
        return [num for num in numbers[28:39] if num > 0]
    else:
        return []