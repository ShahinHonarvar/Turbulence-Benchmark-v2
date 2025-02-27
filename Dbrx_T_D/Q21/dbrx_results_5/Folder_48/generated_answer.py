def all_ints_div_by_num(lst):
    result = []
    for i in range(574, 745):
        num = lst[i]
        if num % 649 == 0:
            result.append(num)
    return result