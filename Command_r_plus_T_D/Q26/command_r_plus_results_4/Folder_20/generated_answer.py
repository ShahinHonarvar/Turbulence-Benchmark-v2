def sum_in_range(numbers_list):
    in_range_sum = 0
    for num in numbers_list:
        if -64 <= num <= 42:
            in_range_sum += num
    return in_range_sum