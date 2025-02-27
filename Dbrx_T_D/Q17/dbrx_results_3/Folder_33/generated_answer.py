def all_ints_div_by_both_two_nums(lst):
    start = 281
    end = 694
    result = []
    for i in range(len(lst)):
        if i < start or i > end:
            continue
        if lst[i] % -722 == 0 and lst[i] % -731 == 0:
            result.append(lst[i])
    return result