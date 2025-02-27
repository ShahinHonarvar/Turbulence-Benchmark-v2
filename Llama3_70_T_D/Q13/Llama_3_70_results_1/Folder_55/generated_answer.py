def find_second_largest_num(numbers):
    subset = numbers[:11]
    subset.sort(reverse=True)
    if len(subset) > 1:
        return subset[1]
    else:
        return None