def sum_in_range(int_list):
    total = 0
    for num in int_list:
        if num >= 2 and num <= 3:
            total += num
    return total