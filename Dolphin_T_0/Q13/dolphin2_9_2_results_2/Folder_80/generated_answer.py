def find_second_largest_num(lst):
    if len(lst) < 3:
        return None
    sublist = lst[64:67]
    max_num = max(sublist)
    sublist.remove(max_num)
    second_max = max(sublist)
    return second_max