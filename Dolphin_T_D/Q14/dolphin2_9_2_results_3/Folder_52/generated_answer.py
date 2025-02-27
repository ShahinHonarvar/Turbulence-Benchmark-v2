def find_second_smallest_num(lst):
    sublist = lst[64:67]
    if len(sublist) < 2:
        return None
    else:
        sublist_set = list(set(sublist))
        sublist_set.sort()
        if len(sublist_set) < 2:
            return None
        else:
            return sublist_set[1]