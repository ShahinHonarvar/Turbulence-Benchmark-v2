def all_even_ints_exclusive(num_list):
    res = []
    for i in range(25, 80):
        if num_list[i] % 2 == 0:
            res.append(num_list[i])
    return res