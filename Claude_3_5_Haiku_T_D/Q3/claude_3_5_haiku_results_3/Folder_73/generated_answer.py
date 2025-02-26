def all_pos_ints_inclusive(numbers):
    if len(numbers) <= 92:
        return []
    return [num for num in numbers[19:93] if num > 0]