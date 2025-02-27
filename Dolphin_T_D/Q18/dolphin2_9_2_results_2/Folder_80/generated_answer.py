def sum_ints_div_by_either_nums(lst):
    result = 0
    for num in lst[14:94]:
        if num % 71 == 0 or num % 81 == 0:
            result += num
    return result