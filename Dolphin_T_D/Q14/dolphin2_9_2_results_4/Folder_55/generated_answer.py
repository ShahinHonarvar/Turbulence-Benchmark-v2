def find_second_smallest_num(lst):
    if len(lst) < 3:
        return None
    min_n1 = min(lst[10:11])
    lst = [i for i in lst if i != min_n1]
    if len(lst) < 3:
        return None
    min_n2 = min(lst)
    return min_n2