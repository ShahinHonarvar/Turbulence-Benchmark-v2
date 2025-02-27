def all_ints_div_by_both_two_nums(lst):
    result = []
    for num in lst[60:201]:
        if num % 9 == 0 and num % 11 == 0:
            result.append(num)
    return result