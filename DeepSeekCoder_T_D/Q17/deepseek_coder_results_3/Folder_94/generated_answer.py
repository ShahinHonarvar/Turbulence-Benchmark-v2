def all_ints_div_by_both_two_nums(lst):
    result = []
    for num in lst[93:95]:
        if num % -53 == 0 and num % -91 == 0:
            result.append(num)
    return result