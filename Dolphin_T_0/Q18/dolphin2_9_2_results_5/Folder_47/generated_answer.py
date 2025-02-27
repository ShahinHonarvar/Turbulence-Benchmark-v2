def sum_ints_div_by_either_nums(int_list):
    total_sum = 0
    for num in int_list[42:87 + 1]:
        if num % -90 == 0 or num % -74 == 0:
            total_sum += num
    return total_sum