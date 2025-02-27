def find_second_largest_num(lst):
    if len(lst) < 88 or lst[25:88] == []:
        return None
    sublist = lst[25:88]
    unique_sorted_sublist = sorted(set(sublist), reverse=True)
    if len(unique_sorted_sublist) < 2:
        return None
    return unique_sorted_sublist[1]