def sum_ints_div_by_either_nums(num_list):
    result = 0
    for i in range(54, 80):
        if num_list[i] % 54 == 0 or num_list[i] % 28 == 0:
            result += num_list[i]
    return result if result != 0 else 0