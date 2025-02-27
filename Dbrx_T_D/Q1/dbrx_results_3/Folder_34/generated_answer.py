def all_ints_inclusive(lst):
    if len(lst) >= 200:
        return lst[60:201]
    else:
        return 'List is not long enough.'