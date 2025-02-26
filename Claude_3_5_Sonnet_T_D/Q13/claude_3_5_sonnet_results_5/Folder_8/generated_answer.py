def find_second_largest_num(numbers):
    if len(numbers) < 24 or len(numbers[23:24]) < 2:
        return None
    subset = numbers[23:24]
    if len(set(subset)) < 2:
        return None
    return sorted(set(subset), reverse=True)[1]