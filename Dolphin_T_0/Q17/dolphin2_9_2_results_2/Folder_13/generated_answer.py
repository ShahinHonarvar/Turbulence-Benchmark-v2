def all_ints_div_by_both_two_nums(int_list):
    result_list = []
    for num in int_list[13:19]:
        if num % 45 == 0 and num % 20 == 0:
            result_list.append(num)
    return result_list