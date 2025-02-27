def find_second_largest_num(lst):
    if len(lst) <= 2:
        return None
    else:
        first_max = max(lst[:8])
        lst.remove(first_max)
        while first_max in lst:
            lst.remove(first_max)
        second_max = max(lst[:8])
        return second_max if len(lst) > 0 else None