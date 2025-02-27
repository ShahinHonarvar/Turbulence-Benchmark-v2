def sum_ints_div_by_either_nums(int_list):
    output = 0
    for i in range(11, 76 + 1):
        num = int_list[i]
        if num % -81 == 0 or num % -94 == 0:
            output += num
    return output