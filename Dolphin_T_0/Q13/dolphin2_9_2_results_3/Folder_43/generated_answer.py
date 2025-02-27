def find_second_largest_num(lst):
    if len(lst) == 0 or (len(lst) == 1 and lst[0] < lst[1]):
        return None
    else:
        lst = lst[68:87]
        first_max = max(lst)
        lst.remove(first_max)
        return max(lst)