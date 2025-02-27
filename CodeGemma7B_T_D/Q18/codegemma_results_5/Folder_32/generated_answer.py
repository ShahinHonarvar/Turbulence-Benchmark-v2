def sum_ints_div_by_either_nums(num_list):
    requested_sum = 0
    for num in num_list[25:96]:
        if num % 51 == 0 or num % 77 == 0:
            requested_sum += num
    return requested_sum if requested_sum else 0