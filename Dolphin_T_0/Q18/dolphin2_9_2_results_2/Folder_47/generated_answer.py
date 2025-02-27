def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in lst[42:88]:
        if i % -90 == 0 or i % -74 == 0:
            total += i
    return total if total != 0 else 0