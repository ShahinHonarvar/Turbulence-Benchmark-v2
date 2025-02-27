def all_ints_div_by_num(input_list):
    result = []
    for i in range(max(0, 42), min(len(input_list), 98)):
        if input_list[i] % 46 == 0:
            result.append(input_list[i])
    return result