def find_second_largest_num(lst):
    sub_lst = lst[4:8]
    if len(sub_lst) < 2:
        return None
    first_largest = max(sub_lst)
    sub_lst.remove(first_largest)
    second_largest = max(sub_lst)
    if sub_lst.count(second_largest) > 1:
        return None
    return second_largest