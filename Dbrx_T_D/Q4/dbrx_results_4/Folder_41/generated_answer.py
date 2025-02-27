def all_pos_ints_exclusive(numbers):
    if len(numbers) > 9:
        return list(filter(lambda x: x > 0, numbers[8:9]))
    else:
        return []