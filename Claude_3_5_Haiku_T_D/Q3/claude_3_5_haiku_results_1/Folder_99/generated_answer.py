def all_pos_ints_inclusive(numbers):
    if len(numbers) <= 370:
        return []
    result = [num for num in numbers[310:371] if num > 0]
    return result