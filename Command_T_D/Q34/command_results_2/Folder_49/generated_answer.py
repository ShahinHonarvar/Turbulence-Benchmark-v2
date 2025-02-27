def find_original_set(s):
    empty_set = set()
    set_set = set()
    for s in s:
        set_set.add(s)
    set_set.add(empty_set)
    return *set_set.intersection(*s)