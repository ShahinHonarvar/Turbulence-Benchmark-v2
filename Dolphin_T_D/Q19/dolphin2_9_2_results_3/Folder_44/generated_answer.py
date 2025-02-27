def all_ints_not_div_by_num(lst):
    result = []
    for num in lst[46:91]:
        if num % 67 != 0:
            result.append(num)
    return result