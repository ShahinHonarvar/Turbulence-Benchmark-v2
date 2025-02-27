def all_pos_ints_inclusive(numbers):
    if len(numbers) < 97:
        return []
    elif len(numbers) > 97:
        numbers = numbers[21:98]
        return [num for num in numbers if num > 0]
    else:
        return numbers[21:98]