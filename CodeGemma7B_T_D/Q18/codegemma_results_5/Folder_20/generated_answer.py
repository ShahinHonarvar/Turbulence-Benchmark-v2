def sum_ints_div_by_either_nums(intlst):
    sum = 0
    for i in range(48, 77):
        if intlst[i] % 46 == 0 or intlst[i] % 82 == 0:
            sum += intlst[i]
    return sum or 0