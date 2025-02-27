def find_second_largest_num(lst):
    if len(lst) < 2:
        return None
    else:
        lst = lst[59:98]
        largest = max(lst)
        lst.remove(largest)
        if len(lst) == 0:
            return None
        else:
            second_largest = max(lst)
            return second_largest