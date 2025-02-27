def all_pos_ints_inclusive(numbers):
    if len(numbers) < 86:
        return []
    positive_numbers = [num for num in numbers[82:87] if num > 0]
    return positive_numbers