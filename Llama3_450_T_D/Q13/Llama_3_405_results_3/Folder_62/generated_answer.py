def find_second_largest_num(lst):
    lst = lst[91:100]
    if len(lst) < 2:
        return None
    else:
        lst.sort(reverse=True)
        return lst[1]