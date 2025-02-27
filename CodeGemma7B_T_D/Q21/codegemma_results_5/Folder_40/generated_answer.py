def all_ints_div_by_num(list):
    new_list = []
    for l in range(len(list)):
        if l % 2 == 0:
            new_list.append(l)
    return new_list