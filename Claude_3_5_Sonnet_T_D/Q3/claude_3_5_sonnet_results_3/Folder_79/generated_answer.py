def all_pos_ints_inclusive(numbers):
    if len(numbers) > 4:
        return [num for num in numbers[4:5] if num > 0]
    else:
        return []