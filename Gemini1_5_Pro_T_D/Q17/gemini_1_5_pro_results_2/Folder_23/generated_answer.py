def all_ints_div_by_both_two_nums(lst):
    result = []
    for i in range(max(69, 0), min(98, len(lst))):
        if lst[i] % -90 == 0 and lst[i] % -67 == 0:
            result.append(lst[i])
    return result