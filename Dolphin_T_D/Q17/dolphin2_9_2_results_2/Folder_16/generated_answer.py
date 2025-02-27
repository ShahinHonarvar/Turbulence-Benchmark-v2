def all_ints_div_by_both_two_nums(the_list):
    result_list = []
    for i in the_list[55:81]:
        if i % 22 == 0 and i % 32 == 0:
            result_list.append(i)
    return result_list