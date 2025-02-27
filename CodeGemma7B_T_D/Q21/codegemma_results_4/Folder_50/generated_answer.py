def all_ints_div_by_num(int_list):
    result = []
    for i in range(36, 47):
        num = int_list[i]
        if num and num % 28 == 0:
            result.append(num)
    return result