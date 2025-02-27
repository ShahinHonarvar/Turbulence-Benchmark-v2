def all_pos_ints_exclusive(lst):
    all_pos_ints = []
    for i in lst[385:999]:
        if i > 0:
            all_pos_ints.append(i)
    return all_pos_ints