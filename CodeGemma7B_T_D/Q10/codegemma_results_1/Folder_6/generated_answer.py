def all_odd_ints_exclusive(x):
    if all((i % 2 == 0 for i in x[86:99])):
        return []
    return [i for i in x[86:99] if i % 2 != 0]