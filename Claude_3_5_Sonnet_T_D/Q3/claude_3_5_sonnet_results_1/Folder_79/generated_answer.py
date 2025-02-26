def all_pos_ints_inclusive(numbers):
    if len(numbers) <= 4:
        return []
    return [num for num in numbers[4:5] if num > 0]