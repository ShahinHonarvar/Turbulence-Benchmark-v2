def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(56, 89):
        num = lst[i]
        if num % -59 == 0 and num % -79 == 0:
            result.append(num)
    return result