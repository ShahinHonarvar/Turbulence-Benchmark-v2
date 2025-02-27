def sum_ints_div_by_either_nums(numlist):
    sum = 0
    for i in range(20, 201):
        if numlist[i] % -20 == 0 or numlist[i] % -200 == 0:
            sum += numlist[i]
    if sum == 0:
        return 0
    return sum