def sum_ints_div_by_either_nums(ints_list):
    total_sum = 0
    for num in ints_list[828:933]:
        if num % -649 == 0 or num % -461 == 0:
            total_sum += num
    return total_sum