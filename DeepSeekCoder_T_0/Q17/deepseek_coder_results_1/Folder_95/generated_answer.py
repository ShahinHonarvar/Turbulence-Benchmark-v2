def all_ints_div_by_both_two_nums(lst):
    result = []
    for num in lst[57:85]:
        if num % -30 == 0 and num % -88 == 0:
            result.append(num)
    return result