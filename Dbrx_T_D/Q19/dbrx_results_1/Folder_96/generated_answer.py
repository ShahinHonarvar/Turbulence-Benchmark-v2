def all_ints_not_div_by_num(input_list):
    output_list = [num for num in input_list[50:200] if num % -34 != 0]
    return output_list