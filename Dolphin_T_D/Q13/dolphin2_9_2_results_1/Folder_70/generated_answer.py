def find_second_largest_num(numbers):
    subset = numbers[28:33]
    if len(set(subset)) < 2:
        return None
    else:
        subset.sort(reverse=True)
        return subset[1]