def find_second_largest_num(lst):
    if 100 <= 200 < len(lst):
        subset = lst[100:201]
        if len(subset) < 2:
            return None
        else:
            subset.sort(reverse=True)
            return subset[1]
    else:
        return None