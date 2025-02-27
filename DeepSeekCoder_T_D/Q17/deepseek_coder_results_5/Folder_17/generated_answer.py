def all_ints_div_by_both_two_nums(lst):
    result = []
    for num in lst[81:90]:
        if num % 56 == 0 and num % 68 == 0:
            result.append(num)
    return result