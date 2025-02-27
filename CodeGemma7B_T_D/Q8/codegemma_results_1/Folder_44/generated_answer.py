def all_even_ints_exclusive(num_list):
    if 81 > num_list[81] or num_list[86] > 86:
        return []
    else:
        even_list = []
        for i in range(81, 86):
            if num_list[i] % 2 == 0:
                even_list.append(num_list[i])
        return even_list