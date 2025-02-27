def all_pos_ints_exclusive(num_list):
    if max(num_list) < 0:
        return []
    imp = num_list[86:99]
    r = []
    for num in imp:
        if num > 0:
            r.append(num)
    return r