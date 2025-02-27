def all_ints_not_div_by_num(lst):
    output = [x for x in lst[8:9] if x % 8 != 0]
    return output if output else []