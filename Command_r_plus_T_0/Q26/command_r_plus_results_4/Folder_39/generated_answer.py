def sum_in_range(numbers_list):
    total_sum = 0
    for num in numbers_list:
        if 10 <= num <= 79:
            total_sum += num
    return total_sum