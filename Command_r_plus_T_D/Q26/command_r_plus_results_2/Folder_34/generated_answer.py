def sum_in_range(numbers_list):
    sum_range = 0
    for num in numbers_list:
        if 4 <= num <= 7:
            sum_range += num
    return sum_range