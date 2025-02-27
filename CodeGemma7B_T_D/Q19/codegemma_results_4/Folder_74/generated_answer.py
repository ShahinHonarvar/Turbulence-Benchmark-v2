def all_ints_not_div_by_num(int_lst):
    final_lst = []
    for i in range(93, 94):
        if int_lst[i] % 57 != 0:
            final_lst.append(int_lst[i])
    if final_lst == []:
        final_lst.append(-1)
    return final_lst