def all_ints_div_by_num(input_list):
    sub_list = input_list[319:613]
    output_list = [num for num in sub_list if num % -215 == 0]
    return output_list