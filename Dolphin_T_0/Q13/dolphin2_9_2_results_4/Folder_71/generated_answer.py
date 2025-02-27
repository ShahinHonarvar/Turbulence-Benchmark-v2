def find_second_largest_num(numbers):
    if not numbers:
        return None
    subset = numbers[25:53]
    if len(set(subset)) <= 1:
        return None
    subset.sort()
    return subset[-2]