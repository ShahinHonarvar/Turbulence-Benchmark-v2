def sum_ints_div_by_either_nums(lst):
    result = 0
    for i in range(10, 77):
        if i < len(lst):
            if lst[i] % -40 == 0 or lst[i] % -12 == 0:
                result += lst[i]
    return result