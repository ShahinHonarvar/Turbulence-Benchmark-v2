def all_ints_div_by_both_two_nums(lst):
    result = []
    for num in lst[11:77]:
        if num % -81 == 0 and num % -94 == 0:
            result.append(num)
    return result