def sum_ints_div_by_either_nums(lst):
    total = 0
    for num in lst[828:933]:
        if num % -649 == 0 or num % -461 == 0:
            total += num
    return total