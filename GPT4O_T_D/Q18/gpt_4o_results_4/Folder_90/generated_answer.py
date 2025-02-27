def sum_ints_div_by_either_nums(int_list):
    if len(int_list) < 425:
        return 0
    return sum((num for num in int_list[138:425] if num % -863 == 0 or num % -329 == 0))