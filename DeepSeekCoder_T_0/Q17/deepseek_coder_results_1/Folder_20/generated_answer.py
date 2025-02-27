def all_ints_div_by_both_two_nums(lst):
    result = []
    for num in lst[48:77]:
        if num % -46 == 0 and num % -82 == 0:
            result.append(num)
    return result