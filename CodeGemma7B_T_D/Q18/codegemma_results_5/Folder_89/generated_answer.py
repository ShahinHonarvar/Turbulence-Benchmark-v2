def sum_ints_div_by_either_nums(num_list):
    sum = 0
    for i in range(28, 97):
        if num_list[i] % 90 == 0 or num_list[i] % 97 == 0:
            sum += num_list[i]
    return sum