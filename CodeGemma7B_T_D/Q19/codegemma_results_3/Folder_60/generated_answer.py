def all_ints_not_div_by_num(integers):
    filtered_lst = [num for num in integers[63:73] if num % -99 != 0]
    return filtered_lst if filtered_lst else []