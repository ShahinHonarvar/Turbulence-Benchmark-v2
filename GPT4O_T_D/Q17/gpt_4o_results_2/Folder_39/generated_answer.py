def all_ints_div_by_both_two_nums(lst):
    result = []
    for num in lst[13:77]:
        if num % -66 == 0 and num % -32 == 0:
            result.append(num)
    return result