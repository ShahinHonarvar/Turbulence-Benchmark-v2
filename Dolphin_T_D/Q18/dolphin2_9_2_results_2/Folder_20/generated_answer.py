def sum_ints_div_by_either_nums(lst):
    sum = 0
    for i in range(48, 77):
        if i % -46 == 0 or i % -82 == 0:
            sum += i
    return sum if sum != 0 else 0