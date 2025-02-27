def all_pos_ints_inclusive(numbers):
    if len(numbers) < 46:
        return []
    elif 1 in numbers[23:46:1] or 2 in numbers[23:46:1] or 3 in numbers[23:46:1]:
        return list(range(1, 24)) + list(range(23, numbers.index(0, 23), 1))
    else:
        return []