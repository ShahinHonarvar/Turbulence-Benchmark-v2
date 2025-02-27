def sum_ints_div_by_either_nums(lst):
    sum = 0
    for i in range(max(24, 0), min(33, len(lst))):
        if lst[i] % 35 == 0 or lst[i] % 87 == 0:
            sum += lst[i]
    return sum