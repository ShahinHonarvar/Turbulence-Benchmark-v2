def all_ints_div_by_both_two_nums(input_list):
    result = []
    for i in range(10, 101):
        if i >= len(input_list):
            break
        if input_list[i] % 10 == 0 and input_list[i] % 100 == 0:
            result.append(input_list[i])
    return result