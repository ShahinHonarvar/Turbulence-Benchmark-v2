def if_perfect_num(lst):
    if len(lst) > 276:
        n = lst[276]
        return n == sum((i for i in range(1, n) if n % i == 0))
    return False