def all_ints_div_by_num(input_list):
    result = []
    for i in range(max(30, len(input_list))):
        if i >= min(300, len(input_list)):
            break
        if input_list[i] % 5 == 0:
            result.append(input_list[i])
    return result