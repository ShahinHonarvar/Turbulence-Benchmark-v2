def sum_in_range(num_list):
    sum = 0
    for num in num_list:
        if num >= 139 and num <= 767:
            sum += num
    return sum if sum else 0