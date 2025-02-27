def all_ints_div_by_both_two_nums(ints):
    output = [i for i in ints[10:77] if i % -40 == 0 and i % -12 == 0]
    return output