def sum_in_range(numbers_list):
    total_sum = 0
    for num in numbers_list:
        if -64 <= num <= 42:
            total_sum += num
    return total_sum