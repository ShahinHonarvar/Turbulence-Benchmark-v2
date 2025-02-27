def all_ints_div_by_num(lst):
    range_list = lst[22:64]
    result = [num for num in range_list if num % -61 == 0]
    return result