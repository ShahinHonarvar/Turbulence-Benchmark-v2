def all_pos_ints_exclusive(the_list):
    if len(the_list) > 93:
        start = the_list[92]
        end = the_list[93]
        return list(range(max(1, start), end))
    else:
        return []