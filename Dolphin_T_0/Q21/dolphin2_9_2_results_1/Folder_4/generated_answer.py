def all_ints_div_by_num(input_list):
    desired_num = -14
    result = []
    for i in range(12, 93):
        if i in input_list and i % desired_num == 0:
            result.append(i)
    return result