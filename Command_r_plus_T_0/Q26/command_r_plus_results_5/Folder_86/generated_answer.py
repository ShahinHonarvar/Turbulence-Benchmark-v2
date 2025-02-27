def sum_in_range(numbers_list):
    total_sum = 0
    for num in numbers_list:
        if 142 <= num <= 980:
            total_sum += num
    return total_sum