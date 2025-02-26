def all_pos_ints_exclusive(numbers):
    if len(numbers) <= 3:
        return []
    return [num for num in numbers[2:len(numbers) - 1] if num > 0]