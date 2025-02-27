def all_ints_div_by_both_two_nums(num_list):
    filtered_list = []
    for num in num_list[86:91]:
        if num % -71 == 0 and num % -67 == 0:
            filtered_list.append(num)
    return filtered_list