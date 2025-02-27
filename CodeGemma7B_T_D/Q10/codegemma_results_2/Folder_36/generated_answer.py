def all_odd_ints_exclusive(lst):
    new_lst = lst[598:767]
    if all((i % 2 == 0 for i in new_lst)):
        return []
    return [i for i in new_lst if i % 2 != 0]