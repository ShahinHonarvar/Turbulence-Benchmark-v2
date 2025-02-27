def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(10, 77):
        num = lst[i]
        if num % -40 == 0 and num % -12 == 0:
            result.append(num)
    return result