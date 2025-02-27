def all_ints_div_by_num(lst):
    result = []
    for num in lst[35:41]:
        if num % 28 == 0:
            result.append(num)
    return result