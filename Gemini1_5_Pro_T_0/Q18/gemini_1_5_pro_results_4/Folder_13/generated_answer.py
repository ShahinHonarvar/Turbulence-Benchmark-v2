def sum_ints_div_by_either_nums(lst):
    sum = 0
    for i in range(max(13, 0), min(19, len(lst))):
        if lst[i] % 45 == 0 or lst[i] % 20 == 0:
            sum += lst[i]
    return sum