def all_ints_div_by_num(num_list):
    new_list = []
    for i in num_list[27:91]:
        if i % 57 == 0:
            new_list.append(i)
    if new_list == []:
        return []
    else:
        return new_list