def find_second_largest_num(lst):
    lst = lst[59:98]
    if len(lst) < 2:
        return None
    else:
        max_num = max(lst)
        lst.remove(max_num)
        if lst:
            return max(lst)
        else:
            return None