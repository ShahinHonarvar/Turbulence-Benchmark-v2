def all_pos_ints_inclusive(numbers):
    if len(numbers) <= 68 or len(numbers) < 42:
        return []
    else:
        return [num for num in numbers[42:69] if num > 0]