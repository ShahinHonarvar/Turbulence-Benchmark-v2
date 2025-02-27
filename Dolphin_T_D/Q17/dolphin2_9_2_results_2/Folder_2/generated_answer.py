def all_ints_div_by_both_two_nums(list):
    range = list[73:87]
    result = [i for i in range if i % 54 == 0 and i % 82 == 0]
    return result