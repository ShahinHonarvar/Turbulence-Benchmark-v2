def all_ints_not_div_by_num(input_list):
    if len(input_list) < 9:
        return []
    output_list = [i for i in input_list[8:9] if i % 3 != 0]
    return output_list