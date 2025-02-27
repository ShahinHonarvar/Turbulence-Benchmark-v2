def all_pos_ints_inclusive(numbers):
    if len(numbers) <= 1 or numbers[0] <= 0:
        return []
    return [num for num in numbers[0:2] if num > 0]