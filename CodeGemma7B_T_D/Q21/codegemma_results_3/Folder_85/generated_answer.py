def all_ints_div_by_num(num_list):
    result_list = []
    for num in num_list[6:9]:
        if num % -9 == 0:
            result_list.append(num)
    if len(result_list) == 0:
        return []
    return result_list