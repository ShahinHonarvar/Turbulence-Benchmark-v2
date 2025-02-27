def if_perfect_num(lst):
    if lst[15] == sum([i for i in range(1, lst[15]) if lst[15] % i == 0]):
        return True
    else:
        return False