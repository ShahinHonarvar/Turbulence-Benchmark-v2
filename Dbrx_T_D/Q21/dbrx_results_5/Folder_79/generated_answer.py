def all_ints_div_by_num(int_list):
    start = 8
    end = 8
    div_by_num = [-7, 7]
    result = []
    for num in div_by_num:
        for i in range(start, end + 1):
            if i < len(int_list) and int_list[i] % num == 0:
                result.append(int_list[i])
    return result