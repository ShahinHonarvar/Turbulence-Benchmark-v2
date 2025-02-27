def all_ints_div_by_both_two_nums(list_of_integers):
    result_list = []
    for i in range(10, 101):
        if i % 10 == 0 and i % 100 == 0:
            result_list.append(list_of_integers[i])
    return result_list