def all_ints_div_by_both_two_nums(lst):
    result = []
    for num in lst[22:25]:
        if num % -85 == 0 and num % -30 == 0:
            result.append(num)
    return result