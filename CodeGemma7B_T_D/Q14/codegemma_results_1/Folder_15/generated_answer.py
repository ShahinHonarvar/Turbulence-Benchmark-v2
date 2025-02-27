def find_second_smallest_num(lst):
    if len(lst) < 3:
        return 'None'
    else:
        lst.sort(reverse=False)
        return lst[2]