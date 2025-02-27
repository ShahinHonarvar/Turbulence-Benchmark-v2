def all_ints_div_by_both_two_nums(lst):
    result = []
    for num in lst[34:82]:
        if num % 27 == 0 and num % 57 == 0:
            result.append(num)
    return result