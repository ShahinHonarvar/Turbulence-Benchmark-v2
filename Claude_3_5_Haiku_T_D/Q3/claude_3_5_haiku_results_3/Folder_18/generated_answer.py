def all_pos_ints_inclusive(numbers):
    if len(numbers) < 50:
        return []
    positive_slice = numbers[35:50]
    return [num for num in positive_slice if num > 0]