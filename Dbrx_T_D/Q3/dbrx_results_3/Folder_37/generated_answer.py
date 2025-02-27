def all_pos_ints_inclusive(numbers):
    if len(numbers) >= 6:
        return [num for num in numbers[1:6] if num > 0]
    else:
        return []