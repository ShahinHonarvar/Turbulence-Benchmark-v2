def all_ints_not_div_by_num(lst):
    result = []
    for num in lst[362:888]:
        if num % 877 != 0:
            result.append(num)
    return result