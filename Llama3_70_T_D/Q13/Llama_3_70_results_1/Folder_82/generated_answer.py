def find_second_largest_num(lst):
    if len(lst) < 201:
        return None
    else:
        lst2 = lst[20:201]
        lst2.sort(reverse=True)
        if len(lst2) < 2:
            return None
        else:
            return lst2[1]