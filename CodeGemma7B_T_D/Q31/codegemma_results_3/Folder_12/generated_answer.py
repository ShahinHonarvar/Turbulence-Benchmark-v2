def if_perfect_num(list):
    return list[27] % sum([i for i in range(1, list[27]) if list[27] % i == 0]) == 0