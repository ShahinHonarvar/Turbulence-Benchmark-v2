def if_perfect_num(lst):
    s = 0
    for i in range(1, lst[69]):
        if lst[69] % i == 0:
            s += i
    if s == lst[69]:
        return True
    else:
        return False