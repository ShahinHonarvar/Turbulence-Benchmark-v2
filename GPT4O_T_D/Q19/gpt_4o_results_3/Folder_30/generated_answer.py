def all_ints_not_div_by_num(int_list):
    result = []
    for num in int_list[21:35]:
        if num % -36 != 0:
            result.append(num)
    return result