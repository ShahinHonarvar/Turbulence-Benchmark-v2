def sum_in_range(numbers_list):
    sum_total = 0
    for num in numbers_list:
        if 7 <= num <= 9:
            sum_total += num
    return sum_total