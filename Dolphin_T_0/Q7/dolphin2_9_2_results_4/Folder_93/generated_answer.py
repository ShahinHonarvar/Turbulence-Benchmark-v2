def all_even_ints_inclusive(lst):
    if 75 <= len(lst) <= 94:
        even_lst = [x for x in lst[75:95] if x % 2 == 0]
        return even_lst
    else:
        return []