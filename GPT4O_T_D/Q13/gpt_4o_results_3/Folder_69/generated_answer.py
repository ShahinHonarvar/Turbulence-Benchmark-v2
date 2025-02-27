def find_second_largest_num(numbers):
    if len(numbers) < 36:
        return None
    subset = numbers[32:36]
    if len(set(subset)) < 2:
        return None
    subset.sort(reverse=True)
    return subset[1]