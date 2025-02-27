def all_ints_div_by_num(int_list):
    result = []
    for i in int_list[0:3]:
        if i % -8 == 0:
            result.append(i)
    return result