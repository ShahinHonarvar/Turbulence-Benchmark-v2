def sum_ints_div_by_either_nums(lst):
    result = 0
    for num in lst[0:3]:
        if num % -2 == 0 or num % 3 == 0:
            result += num
    return result if result != 0 else None