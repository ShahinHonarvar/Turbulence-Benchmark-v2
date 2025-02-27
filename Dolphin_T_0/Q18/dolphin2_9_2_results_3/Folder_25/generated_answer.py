def sum_ints_div_by_either_nums(lst):
    result = 0
    for i in range(25, 81):
        if i in lst:
            if i % -20 == 0 or i % -26 == 0:
                result += i
    return result if result != 0 else 0