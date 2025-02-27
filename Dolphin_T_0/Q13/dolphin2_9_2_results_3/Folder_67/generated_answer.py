def find_second_largest_num(lst):
    if 50 < len(lst):
        sublist = lst[22:51]
        if len(set(sublist)) < 2:
            return None
        else:
            first = max(sublist)
            sublist.remove(first)
            return max(sublist)
    else:
        return None