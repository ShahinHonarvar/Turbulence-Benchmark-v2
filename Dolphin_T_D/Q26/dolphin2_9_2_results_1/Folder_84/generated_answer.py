def sum_in_range(int_list):
    total_sum = 0
    for num in int_list:
        if 113 <= num <= 392:
            total_sum += num
    return total_sum if total_sum > 0 else 0