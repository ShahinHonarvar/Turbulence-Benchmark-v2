def all_ints_not_div_by_num(int_list):
    filtered_list = [num for num in int_list[63:73] if num % -99]
    return [] if not filtered_list else filtered_list