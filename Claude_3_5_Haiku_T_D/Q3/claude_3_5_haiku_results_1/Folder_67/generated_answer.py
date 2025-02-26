def all_pos_ints_inclusive(numbers):
    if len(numbers) <= 22:
        return []
    result = [num for num in numbers[22:51] if num > 0]
    return result