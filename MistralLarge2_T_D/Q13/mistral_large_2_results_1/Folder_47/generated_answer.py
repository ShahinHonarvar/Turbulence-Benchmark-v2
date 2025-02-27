def find_second_largest_num(numbers):
    if len(numbers) < 77:
        return None
    subset = numbers[37:77]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[-2]