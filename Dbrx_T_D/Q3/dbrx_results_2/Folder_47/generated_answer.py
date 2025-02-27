def all_pos_ints_inclusive(numbers):
    if len(numbers) <= 76 or len(numbers) < 37:
        return []
    else:
        return [num for num in numbers[36:77] if num > 0]