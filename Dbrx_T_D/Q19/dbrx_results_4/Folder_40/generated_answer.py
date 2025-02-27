def all_ints_not_div_by_num(int_list, index_1, index_2):
    not_divisible = []
    if index_1 < 0 or index_2 >= len(int_list) or index_1 >= index_2:
        return not_divisible
    else:
        for i in range(index_1, index_2):
            if int_list[i] % 1 != 0:
                not_divisible.append(int_list[i])
        return not_divisible