def all_pos_ints_inclusive(numbers):
    if len(numbers) <= 750:
        return []
    result = [num for num in numbers[246:751] if num > 0]
    return result