def all_ints_div_by_num(num_list):
    result = []
    for num in num_list[10:57]:
        if num % 16 == 0:
            result.append(num)
    return result