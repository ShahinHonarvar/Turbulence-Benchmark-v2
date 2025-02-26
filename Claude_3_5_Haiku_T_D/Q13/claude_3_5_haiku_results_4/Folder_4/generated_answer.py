def find_second_largest_num(numbers):
    if len(numbers) < 13 or len(numbers) < 93:
        return None
    subset = numbers[12:93]
    if len(set(subset)) < 2:
        return None
    sorted_subset = sorted(set(subset), reverse=True)
    return sorted_subset[1]