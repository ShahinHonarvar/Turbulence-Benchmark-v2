def all_ints_div_by_both_two_nums(lst):
    result = []
    for num in lst[306:958]:
        if num % 982 == 0 and num % 319 == 0:
            result.append(num)
    return result