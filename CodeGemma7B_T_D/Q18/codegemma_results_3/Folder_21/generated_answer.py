def sum_ints_div_by_either_nums(lst):
    sum_result = 0
    for num in lst[315:935]:
        if num % -556 == 0 or num % -897 == 0:
            sum_result += num
    if not sum_result:
        return 0
    else:
        return sum_result