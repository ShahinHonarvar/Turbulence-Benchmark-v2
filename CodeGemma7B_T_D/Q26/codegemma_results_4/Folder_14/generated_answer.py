def sum_in_range(int_list):
    sum_result = 0
    for num in int_list:
        if num >= 3 and num <= 7:
            sum_result += num
    return sum_result