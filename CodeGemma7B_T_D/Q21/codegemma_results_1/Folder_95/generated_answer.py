def all_ints_div_by_num(input_list):
    restricted_list = []
    for i in range(75, 86):
        if input_list[i] % -40 == 0:
            restricted_list.append(input_list[i])
    return restricted_list