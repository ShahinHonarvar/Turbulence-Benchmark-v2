def find_second_largest_num(lst):
    if len(lst) <= 2:
        return None
    ant_max = max(lst[80:201])
    lst_new = [i for i in lst[80:201] if i != ant_max]
    return max(lst_new) if lst_new else None