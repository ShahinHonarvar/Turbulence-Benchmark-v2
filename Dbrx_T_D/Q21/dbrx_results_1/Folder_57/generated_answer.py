def all_ints_div_by_num(input_list):
    if len(input_list) < 77 or -92 % len(input_list) != 0:
        return []
    else:
        return [i for i in input_list[70:77] if i % -92 == 0]