def all_ints_div_by_both_two_nums(ints):
    sublist = ints[32:100]
    result = [i for i in sublist if i % -11 == 0 and i % -15 == 0]
    return result if result else []