def all_ints_div_by_both_two_nums(lst):
    result = []
    for num in lst[20:36]:
        if num % -36 == 0 and num % -89 == 0:
            result.append(num)
    return result