def all_ints_div_by_both_two_nums(int_list):
    elems = []
    for i in range(25, 96):
        if int_list[i] % 51 == 0 and int_list[i] % 77 == 0:
            elems.append(int_list[i])
    return elems