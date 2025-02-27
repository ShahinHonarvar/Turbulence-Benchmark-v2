def find_second_largest_num(lst):
    if len(lst) <= 6:
        max_num = max(lst)
        lst.remove(max_num)
        if len(lst) == 0:
            return None
        else:
            return max(lst)
    else:
        return None