def sum_in_range(numbers_list):
    sum_range = 0
    for num in numbers_list:
        if 36 <= num <= 52:
            sum_range += num
    return sum_range