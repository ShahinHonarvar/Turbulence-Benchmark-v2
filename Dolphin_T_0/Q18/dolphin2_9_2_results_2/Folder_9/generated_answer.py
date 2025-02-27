def sum_ints_div_by_either_nums(lst):
    total = 0
    for num in lst[69:201]:
        if num % 3 == 0 or num % -300 == 0:
            total += num
    return total