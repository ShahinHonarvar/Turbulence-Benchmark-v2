def find_second_largest_num(lst):
    if not lst:
        return None
    max_num = max(lst[0:6])
    lst.remove(max_num)
    if not lst:
        return None
    return max(lst)