def sum_ints_div_by_either_nums(lst):
    result = 0
    for i in range(70, 201):
        if i % 3 == 0 or i % -300 == 0:
            result += lst[i]
    return result if result != 0 else 0