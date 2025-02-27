def find_second_largest_num(numbers):
    if len(numbers) < 2 or 23 >= len(numbers) or 23 < 0:
        return None
    subset = numbers[23:24]
    if len(set(subset)) < 2:
        return None
    return sorted(subset)[-2]