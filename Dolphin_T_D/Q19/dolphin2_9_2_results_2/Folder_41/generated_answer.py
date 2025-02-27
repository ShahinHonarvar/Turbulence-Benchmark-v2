def all_ints_not_div_by_num(int_list):
    result = []
    for num in int_list[1:-1]:
        if num % -3 != 0:
            result.append(num)
    return result