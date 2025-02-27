def all_pos_ints_exclusive(numbers):
    if len(numbers) < 6:
        return []
    start = 4
    end = 5
    return [num for num in numbers[start:end] if num > 0]