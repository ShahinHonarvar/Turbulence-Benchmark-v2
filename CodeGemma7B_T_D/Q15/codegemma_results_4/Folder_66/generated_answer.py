def sum_odd_ints_inclusive(num_list):
    sum_odd_nums = 0
    for num in num_list[50:55]:
        if num % 2 != 0:
            sum_odd_nums += num
    if sum_odd_nums == 0:
        return 0
    else:
        return sum_odd_nums