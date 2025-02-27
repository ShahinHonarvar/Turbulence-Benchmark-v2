def all_ints_div_by_both_two_nums(original_list):
    result = []
    for i in range(20, 201):
        if original_list[i] % -20 == 0 and original_list[i] % -200 == 0:
            result.append(original_list[i])
    return result