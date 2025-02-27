def all_ints_div_by_both_two_nums(my_list):
    result = []
    for i in range(0, 2):
        element = my_list[i]
        if element % 6 == 0 and element % 4 == 0:
            result.append(element)
    return result