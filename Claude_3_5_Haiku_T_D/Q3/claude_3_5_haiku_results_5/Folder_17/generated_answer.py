def all_pos_ints_inclusive(numbers):
    if len(numbers) <= 78:
        return []
    positive_ints = [num for num in numbers[62:79] if num > 0]
    return positive_ints