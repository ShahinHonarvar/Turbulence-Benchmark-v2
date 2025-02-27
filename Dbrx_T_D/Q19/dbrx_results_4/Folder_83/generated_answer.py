def all_ints_not_div_by_num(input_list):
    if not input_list[90:200]:
        return []
    else:
        output_list = [i for i in input_list[90:200] if i % -31 != 0]
        return output_list