def find_second_largest_num(lst):
    if len(lst) < 2:
        return None
    else:
        sublist = lst[31:72]
        sublist = list(set(sublist))
        sublist.sort()
        return sublist[-2]