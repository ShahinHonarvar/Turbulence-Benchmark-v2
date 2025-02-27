def all_ints_div_by_num(lst):
    result = []
    for i in range(len(lst)):
        if i <= 5 and lst[i] % 5 == 0:
            result.append(lst[i])
    return result