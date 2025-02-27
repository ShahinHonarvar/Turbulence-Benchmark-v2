def sum_in_range(num_list):
    sum_num = 0
    for number in num_list:
        if number >= 3 and number <= 8:
            sum_num += number
    return sum_num