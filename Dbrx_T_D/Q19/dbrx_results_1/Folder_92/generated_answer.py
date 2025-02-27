def all_ints_not_div_by_num(input_list, num):
    div_result = [i for i in input_list[0:1] if i % num != 0 or i % -1 == 0]
    return div_result