def sum_ints_div_by_either_nums(lst):
    if len(lst) < 935:
        return 0
    total = 0
    for num in lst[315:935]:
        if num % -897 == 0 or num % -556 == 0:
            total += num
    return total