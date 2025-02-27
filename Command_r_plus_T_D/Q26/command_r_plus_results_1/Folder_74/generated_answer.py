def sum_in_range(numbers_list):
    sum_range = 0
    for num in numbers_list:
        if 13 <= num <= 35:
            sum_range += num
    return sum_range