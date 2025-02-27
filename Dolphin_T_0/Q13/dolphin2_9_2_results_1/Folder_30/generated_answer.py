def find_second_largest_num(lst):
    if not lst:
        return None
    max_num = max(lst[55:99])
    lst.remove(max_num)
    if not lst:
        return None
    second_max_num = max(lst)
    return second_max_num