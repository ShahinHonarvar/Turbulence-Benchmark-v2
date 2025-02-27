def all_pos_ints_inclusive(numbers):
    if len(numbers) >= 8:
        return list(filter(lambda x: x > 0, numbers[4:8]))
    else:
        return []