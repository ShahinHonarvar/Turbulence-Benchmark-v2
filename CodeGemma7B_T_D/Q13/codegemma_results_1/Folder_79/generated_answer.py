def find_second_largest_num(lst):
    if len(lst) < 5:
        return None
    lst.sort(reverse=True)
    return lst[4]