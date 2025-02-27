def all_ints_div_by_both_two_nums(lst):
    divisibles = []
    for num in lst[10:77]:
        if num % -81 == 0 and num % -94 == 0:
            divisibles.append(num)
    return divisibles