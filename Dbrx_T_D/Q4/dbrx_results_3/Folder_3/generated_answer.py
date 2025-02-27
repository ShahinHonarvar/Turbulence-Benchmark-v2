def all_pos_ints_exclusive(numbers):
    if 78 < len(numbers) < 93:
        return [num for num in numbers[78:93] if num > 0]
    elif len(numbers) >= 93:
        return [num for num in numbers[78:93] if num > 0]
    else:
        return []