def all_pos_ints_inclusive(numbers):
    if len(numbers) > 8:
        start, end = (4, 8)
        return [num for num in numbers[start:end] if num > 0]
    else:
        return []