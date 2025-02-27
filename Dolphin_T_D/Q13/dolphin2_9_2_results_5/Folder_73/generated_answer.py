def find_second_largest_num(lst):
    if 19 <= len(lst) <= 92:
        sublist = lst[19:93]
        if len(set(sublist)) >= 2:
            max_num = max(sublist)
            sublist.remove(max_num)
            return max(sublist)
    return None