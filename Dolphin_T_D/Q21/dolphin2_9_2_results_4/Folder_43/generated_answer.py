def all_ints_div_by_num(lst):
    result = []
    for num in lst[10:38]:
        if num % -64 == 0:
            result.append(num)
    return result