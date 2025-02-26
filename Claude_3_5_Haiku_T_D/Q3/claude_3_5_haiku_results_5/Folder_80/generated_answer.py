def all_pos_ints_inclusive(numbers):
    if len(numbers) <= 66:
        return []
    result = [num for num in numbers[64:67] if num > 0]
    return result