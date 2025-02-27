def sum_in_range(lst):
    sum_num = 0
    for num in lst:
        if num in range(4, 7):
            sum_num += num
    return sum_num if sum_num != 0 else 0