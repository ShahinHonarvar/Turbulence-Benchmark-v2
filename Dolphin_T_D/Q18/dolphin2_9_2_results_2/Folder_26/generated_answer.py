def sum_ints_div_by_either_nums(lst):
    sum = 0
    for i in lst[69:71]:
        if i % 72 == 0 or i % 70 == 0:
            sum += i
    return sum