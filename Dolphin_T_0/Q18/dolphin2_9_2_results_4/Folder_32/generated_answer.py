def sum_ints_div_by_either_nums(lst):
    relevant_lst = lst[25:96]
    total_sum = 0
    for num in relevant_lst:
        if num % 51 == 0 or num % 77 == 0:
            total_sum += num
    return total_sum