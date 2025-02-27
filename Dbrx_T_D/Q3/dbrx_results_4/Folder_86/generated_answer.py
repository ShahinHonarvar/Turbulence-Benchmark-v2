def all_pos_ints_inclusive(numbers):
    if len(numbers) >= 35:
        return [num for num in numbers[30:35] if num > 0]
    else:
        return []