def all_ints_not_div_by_num(lst):
    result = []
    for num in lst[40:200]:
        if num % 71 != 0:
            result.append(num)
    return result