def sum_in_range(numbers_list):
    sum_total = 0
    for num in numbers_list:
        if 36 <= num <= 52:
            sum_total += num
    return sum_total