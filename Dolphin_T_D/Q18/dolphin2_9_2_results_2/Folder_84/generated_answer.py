def sum_ints_div_by_either_nums(lst):
    result = 0
    for i in range(78, 82):
        if i < len(lst):
            if lst[i] % 76 == 0 or lst[i] % 60 == 0:
                result += lst[i]
    return result