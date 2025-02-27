def all_ints_not_div_by_num(int_list):
    output = [i for i in int_list[38:52] if i % -41 != 0]
    return output if output else []