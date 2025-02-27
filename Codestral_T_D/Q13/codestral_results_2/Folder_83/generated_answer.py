def find_second_largest_num(numbers):
    subset = numbers[90:91]
    if len(subset) < 2:
        return None
    else:
        subset.sort()
        return subset[-2]