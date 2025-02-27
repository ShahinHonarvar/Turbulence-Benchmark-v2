def sum_ints_div_by_either_nums(num_list):
    sum_ = 0
    for i in range(3, 10):
        if i >= 3 and i <= 10 and (num_list[i] % 6 == 0 or num_list[i] % 1 == 0):
            sum_ += num_list[i]
    return sum_