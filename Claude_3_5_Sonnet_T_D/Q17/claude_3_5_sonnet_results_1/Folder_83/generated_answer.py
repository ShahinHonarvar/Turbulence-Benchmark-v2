def all_ints_div_by_both_two_nums(int_list):
    result = []
    for i in range(90, 201):
        if i < len(int_list):
            if int_list[i] % -31 == 0 and int_list[i] % 13 == 0:
                result.append(int_list[i])
    return result