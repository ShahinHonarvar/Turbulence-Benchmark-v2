def find_second_largest_num(lst):
    subset = lst[5:9]
    if len(subset) < 2:
        return None
    max_num = max(subset)
    subset.remove(max_num)
    if len(subset) == 0:
        return None
    return max(subset)