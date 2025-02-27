def all_ints_not_div_by_num(int_list):
    result = []
    for num in int_list[387:516]:
        if num % 310 != 0:
            result.append(num)
    return result