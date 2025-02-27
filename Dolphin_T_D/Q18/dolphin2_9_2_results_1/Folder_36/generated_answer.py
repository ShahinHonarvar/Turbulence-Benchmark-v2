def sum_ints_div_by_either_nums(num_list):
    sum_integers = 0
    for i in range(299, 383):
        if i < len(num_list):
            if num_list[i] % 858 == 0 or num_list[i] % 952 == 0:
                sum_integers += num_list[i]
    return sum_integers