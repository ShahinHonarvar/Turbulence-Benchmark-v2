def sum_ints_div_by_either_nums(lst):
    if len(lst) <= 35:
        return 0
    div_sum = 0
    for num in lst[20:36]:
        if num % -36 == 0 or num % -89 == 0:
            div_sum += num
    return div_sum