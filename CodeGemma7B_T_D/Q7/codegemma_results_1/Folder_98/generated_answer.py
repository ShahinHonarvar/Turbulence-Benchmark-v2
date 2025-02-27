def all_even_ints_inclusive(lst):
    if not any((x % 2 == 0 for x in lst[0:7])):
        return []
    return lst[0:7:2]