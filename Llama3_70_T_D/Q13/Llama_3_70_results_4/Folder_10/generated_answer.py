def find_second_largest_num(lst):
    if len(lst) < 60:
        return None
    sublist = lst[25:60]
    largest = max(sublist)
    sublist = [x for x in sublist if x != largest]
    if sublist:
        return max(sublist)
    else:
        return None