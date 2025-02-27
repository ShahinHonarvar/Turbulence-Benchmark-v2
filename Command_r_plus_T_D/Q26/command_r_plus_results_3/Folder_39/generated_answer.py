def sum_in_range(numbers_list):
    sum_range = 0
    for num in numbers_list:
        if 10 <= num <= 79:
            sum_range += num
    return sum_range