def sum_in_range(int_list):
    sum = 0
    for num in int_list:
        if num >= 18 and num <= 52:
            sum += num
    return sum