def sum_in_range(num_list):
    sum_within_range = 0
    for num in num_list:
        if 3 <= num <= 5:
            sum_within_range += num
    if sum_within_range == 0:
        return 0
    else:
        return sum_within_range