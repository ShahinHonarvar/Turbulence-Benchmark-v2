def sum_ints_div_by_either_nums(lst):
    total_sum = 0
    for num in lst[22:25]:
        if num % -85 == 0 or num % -30 == 0:
            total_sum += num
    return total_sum if total_sum != 0 else 0