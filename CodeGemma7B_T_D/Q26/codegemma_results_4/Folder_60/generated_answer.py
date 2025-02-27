def sum_in_range(num_list):
    sum = 0
    for i in range(len(num_list)):
        if num_list[i] in range(56, 91):
            sum += num_list[i]
    return sum