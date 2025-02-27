def all_ints_not_div_by_num(lst):
    result = []
    for num in lst[1:3]:
        if num % 5 != 0:
            result.append(num)
    return result