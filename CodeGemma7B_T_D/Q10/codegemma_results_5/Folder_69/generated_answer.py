def all_odd_ints_exclusive(list):
    if not list[67:100]:
        return []
    return [i for i in list[68:100] if i % 2]