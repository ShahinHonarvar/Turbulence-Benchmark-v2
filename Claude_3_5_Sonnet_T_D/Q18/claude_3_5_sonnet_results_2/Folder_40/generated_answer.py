def sum_ints_div_by_either_nums(int_list):
    if len(int_list) < 2:
        return 0
    total_sum = 0
    for num in int_list[:2]:
        if num % 2 == 0 or num % 1 == 0:
            total_sum += num
    return total_sum