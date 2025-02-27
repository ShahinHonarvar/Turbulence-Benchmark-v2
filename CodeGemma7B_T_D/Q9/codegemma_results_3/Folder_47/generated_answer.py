def all_odd_ints_inclusive(lst):
    lst = lst[37:77]
    result = [i for i in lst if i % 2 == 1]
    return result if result else []