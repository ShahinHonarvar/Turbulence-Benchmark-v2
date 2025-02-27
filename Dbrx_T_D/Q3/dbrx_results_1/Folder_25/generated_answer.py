def all_pos_ints_inclusive(numbers):
    if len(numbers) >= 94 and all((isinstance(i, int) for i in numbers[28:94])):
        return [i for i in numbers[28:94] if i > 0]
    else:
        return []