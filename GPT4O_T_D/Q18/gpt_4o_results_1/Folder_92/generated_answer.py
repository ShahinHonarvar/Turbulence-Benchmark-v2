def sum_ints_div_by_either_nums(int_list):
    if len(int_list) == 0:
        return 0
    num = int_list[0]
    if num % 1 == 0 or num % -1 == 0:
        return num
    return 0