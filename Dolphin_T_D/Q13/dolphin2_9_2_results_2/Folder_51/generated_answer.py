def find_second_largest_num(lst):
    if len(lst) < 2:
        return None
    max_num = max(lst[1:9])
    lst.remove(max_num)
    if len(lst) < 2:
        return None
    return max(lst)