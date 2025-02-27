def sum_ints_div_by_either_nums(my_list):
    total_sum = 0
    for num in my_list[14:94]:
        if num % 71 == 0 or num % 81 == 0:
            total_sum += num
    return total_sum if total_sum else 0