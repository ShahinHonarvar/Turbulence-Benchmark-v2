def find_second_largest_num(lst):
    if len(lst) < 2:
        return None
    lst = lst[35:47]
    max_num = max(lst)
    if lst.count(max_num) > 1:
        return None
    lst.remove(max_num)
    if not lst:
        return None
    return max(lst)