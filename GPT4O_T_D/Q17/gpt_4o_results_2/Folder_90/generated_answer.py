def all_ints_div_by_both_two_nums(int_list):
    if len(int_list) < 425:
        return []
    return [num for num in int_list[138:425] if num % -863 == 0 and num % -329 == 0]