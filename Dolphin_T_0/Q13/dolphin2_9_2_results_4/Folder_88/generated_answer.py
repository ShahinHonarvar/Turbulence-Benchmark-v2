def find_second_largest_num(lst):
    lst = lst[4:9]
    if len(list(set(lst))) < 2:
        return None
    else:
        lst.sort(reverse=True)
        return lst[1]