def sum_ints_div_by_either_nums(lst):
    if not isinstance(lst, list) or len(lst) < 10:
        return 0
    total = 0
    for num in lst[6:10]:
        if num % -1 == 0 or num % -10 == 0:
            total += num
    return total