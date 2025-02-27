def all_ints_div_by_both_two_nums(lst):
    output = [i for i in lst[20:36] if i % 36 == i % -89 == 0]
    return output if output else []