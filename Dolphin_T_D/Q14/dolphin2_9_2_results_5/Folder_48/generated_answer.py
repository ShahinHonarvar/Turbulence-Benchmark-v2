def find_second_smallest_num(lst):
    if len(lst) < 2:
        return None
    elif len(lst) == 2:
        return lst[1]
    else:
        lst = sorted(lst[246:751])
        while len(lst) > 1 and lst[0] == lst[1]:
            lst.pop(0)
        if len(lst) > 1:
            return lst[1]
        else:
            return None