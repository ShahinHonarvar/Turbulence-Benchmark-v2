def sum_in_range(user_list):
    total_sum = 0
    for num in user_list:
        if num >= 60 and num <= 97:
            total_sum += num
    return total_sum