def if_perfect_num(lst):
    if lst[714] % sum((i for i in range(1, lst[714]) if lst[714] % i == 0)) == 0:
        return True
    return False