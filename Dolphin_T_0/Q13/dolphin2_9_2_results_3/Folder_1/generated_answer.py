def find_second_largest_num(lst):
    if len(lst) < 2:
        return None
    max1 = max(lst[31:73])
    lst = [i for i in lst[31:73] if i != max1]
    if len(lst) < 2:
        return None
    max2 = max(lst)
    return max2