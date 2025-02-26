def all_pos_ints_inclusive(numbers):
    if len(numbers) <= 88:
        return []
    result = [num for num in numbers[75:89] if num > 0]
    return result