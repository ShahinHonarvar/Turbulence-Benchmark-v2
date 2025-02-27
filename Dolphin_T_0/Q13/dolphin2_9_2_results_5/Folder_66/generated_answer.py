def find_second_largest_num(lst):
    sublist = lst[50:55]
    if len(set(sublist)) < 2:
        return None
    else:
        sublist.sort()
        return sublist[-2]