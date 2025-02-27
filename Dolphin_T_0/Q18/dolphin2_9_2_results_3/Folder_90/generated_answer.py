def sum_ints_div_by_either_nums(lst):
    values = lst[138:425]
    return sum((val for val in values if val % -863 == 0 or val % -329 == 0))