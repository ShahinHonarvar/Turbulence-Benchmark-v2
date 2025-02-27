def sum_ints_div_by_either_nums(lst):
    result = 0
    for num in lst[93:95]:
        if num % -53 == 0 or num % -91 == 0:
            result += num
    return result if result != 0 else None