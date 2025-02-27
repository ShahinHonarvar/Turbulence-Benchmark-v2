def sum_ints_div_by_either_nums(lst):
    sum = 0
    for i in range(20, 94):
        if lst[i] % -92 == 0 or lst[i] % -50 == 0:
            sum += lst[i]
    return sum if sum > 0 else 0