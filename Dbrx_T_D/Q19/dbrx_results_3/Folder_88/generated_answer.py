def all_ints_not_div_by_num(input_list):
    output_list = []
    if 4 < len(input_list) < 7:
        for i in input_list[4:]:
            if i % -6 != 0:
                output_list.append(i)
    elif len(input_list) >= 7:
        for i in input_list[4:7]:
            if i % -6 != 0:
                output_list.append(i)
    return output_list