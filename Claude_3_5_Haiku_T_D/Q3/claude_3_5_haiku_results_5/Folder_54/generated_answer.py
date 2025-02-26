def all_pos_ints_inclusive(numbers):
    if len(numbers) <= 55:
        return []
    positive_ints = [num for num in numbers[34:56] if num > 0]
    return positive_ints