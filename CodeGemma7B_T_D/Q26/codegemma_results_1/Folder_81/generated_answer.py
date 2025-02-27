def sum_in_range(int_list):
    total_sum = 0
    for num in int_list:
        if 3 <= num <= 5:
            total_sum += num
    if total_sum == 0:
        return 0
    else:
        return total_sum