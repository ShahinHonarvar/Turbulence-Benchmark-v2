def all_ints_div_by_both_two_nums(lst):
    result = []
    for num in lst[51:77]:
        if num % -90 == 0 and num % -59 == 0:
            result.append(num)
    return result