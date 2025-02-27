def all_ints_div_by_num(input_list):
    result = []
    for i in range(max(816, 0), min(883, len(input_list) - 1) + 1):
        if input_list[i] % -586 == 0:
            result.append(input_list[i])
    return result