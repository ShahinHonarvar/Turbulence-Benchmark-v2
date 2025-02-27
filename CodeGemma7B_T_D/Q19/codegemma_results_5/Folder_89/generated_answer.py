def all_ints_not_div_by_num(lst):
    result = []
    for num in lst[48:62]:
        if num % 28 != 0:
            result.append(num)
    return result