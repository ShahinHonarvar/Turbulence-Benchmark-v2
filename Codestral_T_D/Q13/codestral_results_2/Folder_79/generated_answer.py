def find_second_largest_num(numbers):
    subset = sorted(numbers[4:5])
    return subset[-2] if len(subset) > 1 else None