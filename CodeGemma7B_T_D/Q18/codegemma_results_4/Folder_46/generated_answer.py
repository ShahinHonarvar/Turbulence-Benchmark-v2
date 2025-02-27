def sum_ints_div_by_either_nums(num_list):
    sum = 0
    count = 0
    for i in range(11, 47):
        if num_list[i] % 55 == 0 or num_list[i] % 36 == 0:
            sum += num_list[i]
            count += 1
    if count == 0:
        return 0
    else:
        return sum