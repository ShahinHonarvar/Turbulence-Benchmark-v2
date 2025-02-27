def find_second_smallest_num(lst):
    sublist = lst[608:609]
    if len(sublist) >= 2:
        sorted_sublist = sorted(sublist)
        return sorted_sublist[1]
    else:
        return None