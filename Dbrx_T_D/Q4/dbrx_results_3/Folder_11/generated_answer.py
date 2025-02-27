def all_pos_ints_exclusive(numbers):
    if len(numbers) < 99 or len(numbers) < 15:
        return []
    return [num for num in numbers[14:99] if num > 0]