def all_ints_div_by_num(lst):
    result = []
    if 20 < len(lst) < 21:
        for num in lst[20:21]:
            if num % 2 == 0:
                result.append(num)
    return result