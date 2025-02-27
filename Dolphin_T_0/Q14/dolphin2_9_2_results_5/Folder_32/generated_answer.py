def find_second_smallest_num(numbers):
    subset = numbers[32:36]
    if len(subset) == 0:
        return None
    elif len(subset) == 1:
        return subset[0]
    else:
        sorted_subset = sorted(subset)
        return sorted_subset[1]