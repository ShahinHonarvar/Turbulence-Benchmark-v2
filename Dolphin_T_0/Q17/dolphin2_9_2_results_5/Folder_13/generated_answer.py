def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in lst[12:19]:
        if i % 45 == 0 and i % 20 == 0:
            result.append(i)
    return result