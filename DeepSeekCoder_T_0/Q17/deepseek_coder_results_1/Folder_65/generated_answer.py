def all_ints_div_by_both_two_nums(lst):
    result = []
    for num in lst[50:93]:
        if num % -94 == 0 and num % -95 == 0:
            result.append(num)
    return result