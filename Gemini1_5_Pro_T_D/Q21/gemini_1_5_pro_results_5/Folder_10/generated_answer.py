def all_ints_div_by_num(input_list):
    result = []
    for i in range(max(42, 0), min(len(input_list), 90)):
        if input_list[i] % -59 == 0:
            result.append(input_list[i])
    return result