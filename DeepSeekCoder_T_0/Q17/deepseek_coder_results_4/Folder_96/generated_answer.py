def all_ints_div_by_both_two_nums(lst):
    result = []
    for num in lst[50:201]:
        if num % -34 == 0 and num % 64 == 0:
            result.append(num)
    return result