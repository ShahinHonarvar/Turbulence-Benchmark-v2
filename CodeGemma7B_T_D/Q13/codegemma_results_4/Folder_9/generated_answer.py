def find_second_largest_num(lst):
    lst.sort()
    try:
        return lst[200]
    except IndexError:
        return None