def all_pos_ints_inclusive(numbers):
    if len(numbers) >= 79:
        return list(filter(lambda x: x > 0, numbers[16:79]))
    else:
        return []