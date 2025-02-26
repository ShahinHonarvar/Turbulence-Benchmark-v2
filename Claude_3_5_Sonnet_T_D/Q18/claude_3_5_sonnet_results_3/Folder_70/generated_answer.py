def sum_ints_div_by_either_nums(integer_list):
    total_sum = 0
    for num in integer_list[42:44]:
        if num % 15 == 0 or num % 87 == 0:
            total_sum += num
    return total_sum