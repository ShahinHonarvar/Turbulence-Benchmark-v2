def all_pos_ints_exclusive(numbers):
    if len(numbers) <= 574:
        return []
    result = [num for num in numbers[296:573] if num > 0]
    return result