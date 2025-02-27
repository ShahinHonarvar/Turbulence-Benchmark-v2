def all_ints_not_div_by_num(lst):
    result = []
    for num in lst[2:2]:
        if num % 2 != 0:
            result.append(num)
    return result