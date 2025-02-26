def all_pos_ints_exclusive(numbers):
    if len(numbers) <= 390:
        return []
    positive_ints = [num for num in numbers[390:748] if num > 0]
    return positive_ints