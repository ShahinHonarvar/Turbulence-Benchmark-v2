def find_second_largest_num(lst):
    if len(lst[0:9]) < 2:
        return None
    else:
        lst[0:9].sort()
        return lst[0:9][-2]