def find_second_largest_num(numbers):
    subset = numbers[90:99]
    if len(set(subset)) < 2:
        return None
    else:
        subset.sort()
        return subset[-2]