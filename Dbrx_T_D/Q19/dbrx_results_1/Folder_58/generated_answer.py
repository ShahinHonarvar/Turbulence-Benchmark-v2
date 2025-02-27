def all_ints_not_div_by_num(input_list):
    result = [i for i in input_list[266:586] if i % 840 != 0]
    return result