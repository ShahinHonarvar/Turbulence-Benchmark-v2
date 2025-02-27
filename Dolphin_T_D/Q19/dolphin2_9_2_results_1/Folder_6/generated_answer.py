def all_ints_not_div_by_num(lst):
    result = []
    for num in lst[43:70]:
        if num % 69 != 0:
            result.append(num)
    return result