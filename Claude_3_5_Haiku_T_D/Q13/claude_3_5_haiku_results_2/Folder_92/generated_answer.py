def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    subset = numbers[0:2]
    if len(set(subset)) < 2:
        return None
    return sorted(subset)[-2]