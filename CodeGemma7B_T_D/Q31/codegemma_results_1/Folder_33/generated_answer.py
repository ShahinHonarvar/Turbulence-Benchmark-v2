def if_perfect_num(num_list):
    if num_list[321] in [i * (i + 1) // 2 for i in range(1, int(num_list[321] ** (1 / 2)) + 1)]:
        return True
    return False