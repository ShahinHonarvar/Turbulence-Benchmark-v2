def all_ints_div_by_both_two_nums(lst):
    result = []
    for num in lst[72:94]:
        if num % 32 == 0 and num % 44 == 0:
            result.append(num)
    return result