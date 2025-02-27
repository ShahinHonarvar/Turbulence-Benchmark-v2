def sum_ints_div_by_either_nums(lst):
    sublist = lst[90:98]
    result = 0
    for num in sublist:
        if num % 13 == 0 or num % 35 == 0:
            result += num
    return result