def sum_ints_div_by_either_nums(lst):
    total = 0
    for num in lst[138:425]:
        if num % -863 == 0 or num % -329 == 0:
            total += num
    return total if total != 0 else 0