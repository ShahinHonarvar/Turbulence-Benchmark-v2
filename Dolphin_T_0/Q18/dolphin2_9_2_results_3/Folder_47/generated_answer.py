def sum_ints_div_by_either_nums(lst):
    total = 0
    for num in lst[42:87]:
        if num % -90 == 0 or num % -74 == 0:
            total += num
    return total if total != 0 else None