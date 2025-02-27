def find_second_smallest_num(lst):
    lst.sort()
    try:
        return lst[4]
    except IndexError:
        return None