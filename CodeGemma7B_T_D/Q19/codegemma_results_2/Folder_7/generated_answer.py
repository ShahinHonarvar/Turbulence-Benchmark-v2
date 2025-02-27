def all_ints_not_div_by_num(num_list):
    result_list = []
    for num in num_list[495:826]:
        if num % -201 != 0:
            result_list.append(num)
    return result_list