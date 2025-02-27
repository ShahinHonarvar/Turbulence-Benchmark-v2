def sum_ints_div_by_either_nums(lst):
    result = 0
    for i in range(28, 97):
        if i % 90 == 0 or i % 97 == 0:
            result += lst[i]
    return result