def all_ints_div_by_num(input_list):
    result = []
    for i in range(max(0, 33), min(len(input_list), 36)):
        if input_list[i] % 91 == 0:
            result.append(input_list[i])
    return result