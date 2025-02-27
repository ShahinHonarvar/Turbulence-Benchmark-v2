def sum_ints_div_by_either_nums(lst):
    result = 0
    for num in lst[81:90]:
        if num % 56 == 0 or num % 68 == 0:
            result += num
    return result