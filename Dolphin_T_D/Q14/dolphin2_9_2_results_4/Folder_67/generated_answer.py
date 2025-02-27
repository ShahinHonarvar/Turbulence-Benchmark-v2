def find_second_smallest_num(numbers):
    subset = numbers[50:55]
    if len(set(subset)) < 2:
        return None
    subset.sort()
    return subset[1]