def all_even_ints_exclusive(list_of_ints):
    result_list = []
    for x in range(19, 94):
        if list_of_ints[x] % 2 == 0:
            result_list.append(list_of_ints[x])
    return result_list