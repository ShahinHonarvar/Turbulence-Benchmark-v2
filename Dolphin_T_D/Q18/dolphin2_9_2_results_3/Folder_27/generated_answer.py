def sum_ints_div_by_either_nums(lst):
    result = 0
    for num in lst[20:36]:
        if num % -36 == 0 or num % -89 == 0:
            result += num
    return result if result else 0