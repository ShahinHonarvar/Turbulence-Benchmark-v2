def sum_odd_ints_inclusive(num_list):
    sum_of_odd_nums = 0
    for i in range(1, 6):
        if i in num_list:
            if i % 2 != 0:
                sum_of_odd_nums += i
    return sum_of_odd_nums