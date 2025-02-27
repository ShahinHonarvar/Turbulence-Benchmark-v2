def all_ints_div_by_both_two_nums(lst):
    result = []
    for num in lst[30:201]:
        if num % 115 == 0 and num % -115 == 0:
            result.append(num)
    return result