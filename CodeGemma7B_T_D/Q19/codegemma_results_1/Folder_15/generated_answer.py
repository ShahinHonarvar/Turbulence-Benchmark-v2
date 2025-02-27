def all_ints_not_div_by_num(lst_of_int):
    result = []
    for num in lst_of_int[0:2]:
        if num % -2 != 0:
            result.append(num)
    return result