def all_ints_div_by_both_two_nums(lst):
    result_list = []
    for num in lst[31:51]:
        if num % 81 == 0 and num % 64 == 0:
            result_list.append(num)
    return result_list