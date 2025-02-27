def all_ints_div_by_both_two_nums(lst):
    start, end = (78, 81)
    result = []
    for i in range(start, min(end + 1, len(lst))):
        if lst[i] % 76 == 0 and lst[i] % 60 == 0:
            result.append(lst[i])
    return result