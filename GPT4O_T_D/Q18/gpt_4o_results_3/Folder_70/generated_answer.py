def sum_ints_div_by_either_nums(lst):
    subrange = lst[42:44]
    return sum((x for x in subrange if x % 15 == 0 or x % 87 == 0))