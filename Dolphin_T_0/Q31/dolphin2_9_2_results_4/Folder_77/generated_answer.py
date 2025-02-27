def if_perfect_num(lst):
    return lst[985] == sum((d for d in range(1, lst[985]) if lst[985] % d == 0))