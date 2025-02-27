def find_second_largest_num(lst):
    sublist = lst[91:100]
    if len(sublist) < 2:
        return None
    else:
        sorted_sublist = sorted(sublist, reverse=True)
        return sorted_sublist[1]