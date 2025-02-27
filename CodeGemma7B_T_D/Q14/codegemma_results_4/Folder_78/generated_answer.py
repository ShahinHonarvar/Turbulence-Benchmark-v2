def find_second_smallest_num(lst):
    try:
        lst = lst[17:79]
        lst.sort()
        return lst[1]
    except:
        return 'None'