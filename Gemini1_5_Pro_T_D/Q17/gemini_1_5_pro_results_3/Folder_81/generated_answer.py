def all_ints_div_by_both_two_nums(int_list):
    result = []
    for i in range(10, 101):
        if i >= len(int_list):
            break
        if int_list[i] % 10 == 0 and int_list[i] % 100 == 0:
            result.append(int_list[i])
    return result