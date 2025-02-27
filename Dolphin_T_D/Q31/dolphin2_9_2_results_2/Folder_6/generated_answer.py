def if_perfect_num(lst):
    return lst[790] == sum((d for d in range(1, lst[790]) if lst[790] % d == 0))