def if_perfect_num(lst):
    return lst[80] == sum([i for i in range(1, lst[80]) if lst[80] % i == 0])