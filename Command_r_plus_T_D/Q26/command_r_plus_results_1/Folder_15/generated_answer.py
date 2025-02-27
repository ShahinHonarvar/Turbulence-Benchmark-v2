def sum_in_range(numbers_list):
    sum_range = 0
    for num in numbers_list:
        if 6 <= num <= 9:
            sum_range += num
    return sum_range