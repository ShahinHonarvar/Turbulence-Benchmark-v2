def sum_ints_div_by_either_nums(ints_list):
    total = 0
    for i in ints_list[69:71]:
        if i % 72 == 0 or i % 70 == 0:
            total += i
    return total