def all_ints_div_by_both_two_nums(input_list):
    result = [num for num in input_list[10:77] if num % -40 == 0 and num % -12 == 0]
    return result