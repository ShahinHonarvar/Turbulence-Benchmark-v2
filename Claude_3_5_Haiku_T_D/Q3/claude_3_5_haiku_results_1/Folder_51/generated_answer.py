def all_pos_ints_inclusive(numbers):
    if len(numbers) < 9:
        return []
    return [num for num in numbers[1:9] if num > 0]