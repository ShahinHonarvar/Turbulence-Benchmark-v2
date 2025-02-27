def sum_ints_div_by_either_nums(integers):
    subset = integers[55:85]
    result = sum((i for i in subset if i % -24 == 0 or i % -11 == 0))
    return result