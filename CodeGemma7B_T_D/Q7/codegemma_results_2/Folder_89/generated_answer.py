def all_even_ints_inclusive(int_list):
    result_list = []
    for i in range(56, 83):
        if int_list[i] % 2 == 0:
            result_list.append(int_list[i])
    return result_list