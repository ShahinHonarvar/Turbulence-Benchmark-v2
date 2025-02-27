def find_second_largest_num(lst):
    if not lst:
        return None
    lst_shorted = [x for x in lst[62:79] if x != max(lst[62:79])]
    return max(lst_shorted) if lst_shorted else None