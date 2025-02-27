def all_ints_div_by_both_two_nums(lst):
    result = []
    for int in lst[0:5]:
        if int % 8 == 0 and int % -3 == 0:
            result.append(int)
    return result