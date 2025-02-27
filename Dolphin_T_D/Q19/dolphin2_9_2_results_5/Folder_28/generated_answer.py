def all_ints_not_div_by_num(integers):
    specified_range = integers[82:86]
    result = [x for x in specified_range if x % 77 != 0]
    return result