def find_second_largest_num(lst):
    try:
        lst = lst[20:31]
        lst.sort()
        return lst[-2]
    except:
        return None