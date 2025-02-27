def all_ints_not_div_by_num(input_list):
    if len(input_list) < 200:
        return []
    output_list = [i for i in input_list[60:200] if i % 9 != 0]
    return output_list