def all_pos_ints_inclusive(numbers):
    if len(numbers) >= 9:
        return [num for num in numbers[4:9] if num > 0]
    else:
        return []