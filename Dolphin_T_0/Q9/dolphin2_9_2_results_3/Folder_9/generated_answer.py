def all_odd_ints_inclusive(lst):
    result = [x for x in lst[70:201] if x % 2 != 0]
    return result if result else []