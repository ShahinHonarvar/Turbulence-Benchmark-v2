def all_ints_div_by_both_two_nums(lst):
    result = []
    for num in lst[81:87]:
        if num % -33 == 0 and num % -62 == 0:
            result.append(num)
    return result