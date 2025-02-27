def sum_in_range(numbers_list):
    sum_range = 0
    for num in numbers_list:
        if -100 <= num <= -55:
            sum_range += num
    return sum_range