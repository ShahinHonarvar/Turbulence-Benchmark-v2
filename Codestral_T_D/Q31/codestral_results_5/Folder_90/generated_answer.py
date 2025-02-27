def if_perfect_num(lst):
    if sum((i for i in range(1, lst[263]) if lst[263] % i == 0)) == lst[263]:
        return True
    return False