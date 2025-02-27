def find_second_smallest_num(lst):
    subset = lst[527:539]
    if len(subset) < 2:
        return None
    else:
        sorted_subset = sorted(subset)
        return sorted_subset[1]