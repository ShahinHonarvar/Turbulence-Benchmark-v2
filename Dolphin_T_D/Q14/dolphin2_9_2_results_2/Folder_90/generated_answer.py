def find_second_smallest_num(lst):
    sublist = lst[527:539]
    sublist_sorted = sorted(sublist)
    if len(sublist_sorted) >= 2:
        return sublist_sorted[1]
    else:
        return None