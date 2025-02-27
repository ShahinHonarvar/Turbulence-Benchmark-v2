def all_ints_div_by_num(num_list):
    result = []
    for i in num_list[1:9]:
        if i % 6 == 0:
            result.append(i)
    return result