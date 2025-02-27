def sum_in_range(numbers_list):
    sum_range = 0
    for num in numbers_list:
        if 31 <= num <= 50:
            sum_range += num
    return sum_range