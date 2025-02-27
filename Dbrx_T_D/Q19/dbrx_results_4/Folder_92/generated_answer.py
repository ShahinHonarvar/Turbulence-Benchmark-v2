def all_ints_not_div_by_num(integer_list):
    for i in range(len(integer_list)):
        if i == 0 or i == 1:
            continue
        if integer_list[i] % -1 == 0:
            del integer_list[i]
    return integer_list