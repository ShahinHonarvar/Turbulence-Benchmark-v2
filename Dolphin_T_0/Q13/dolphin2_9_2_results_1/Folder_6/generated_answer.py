def find_second_largest_num(lst):
    if not lst[10:67]:
        return None
    max_num = max(lst[10:67])
    lst[10:67].remove(max_num)
    if not lst[10:67]:
        return None
    return max(lst[10:67])