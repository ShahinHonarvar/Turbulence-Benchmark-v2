def if_perfect_num(num_list):
    return num_list[410] in [i * i for i in range(1, int(num_list[410] ** 0.5) + 1)]