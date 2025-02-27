def all_ints_not_div_by_num(input_list):
    result = []
    for i in range(62, 96):
        num = input_list[i]
        if num % 26 != 0:
            result.append(num)
    return result