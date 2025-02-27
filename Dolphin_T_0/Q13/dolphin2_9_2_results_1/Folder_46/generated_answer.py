def find_second_largest_num(lst):
    if 30 <= 87 < len(lst):
        sublist = lst[30:88]
        if len(set(sublist)) >= 2:
            sublist.sort()
            return sublist[-2]
    return None