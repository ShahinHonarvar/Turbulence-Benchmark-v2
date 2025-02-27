def find_second_largest_num(lst):
    if len(lst) == 0:
        return None
    max1 = max(lst[59:98])
    lst = [i for i in lst if i != max1]
    if len(lst) == 0:
        return None
    return max(lst[59:98])