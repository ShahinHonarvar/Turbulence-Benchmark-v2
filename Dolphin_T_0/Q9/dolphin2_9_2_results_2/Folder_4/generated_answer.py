def all_odd_ints_inclusive(lst):
    result = [i for i in lst[12:93] if i % 2 != 0]
    return result if result else []