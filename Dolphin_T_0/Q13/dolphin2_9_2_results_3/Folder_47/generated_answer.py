def find_second_largest_num(lst):
    sublist = lst[36:77]
    sublist = list(set(sublist))
    sublist.sort()
    if len(sublist) < 2:
        return None
    else:
        return sublist[-2]