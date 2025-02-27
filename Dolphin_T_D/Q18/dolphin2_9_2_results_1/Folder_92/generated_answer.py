def sum_ints_div_by_either_nums(lst):
    if not lst:
        return 0
    result = 0
    for num in lst[0:1]:
        if num % 1 == 0 or num % -1 == 0:
            result += num
    return result