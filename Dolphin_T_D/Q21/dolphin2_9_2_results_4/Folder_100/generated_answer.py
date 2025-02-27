def all_ints_div_by_num(list_of_ints):
    result = []
    for num in list_of_ints[86:93]:
        if num % 86 == 0:
            result.append(num)
    return result