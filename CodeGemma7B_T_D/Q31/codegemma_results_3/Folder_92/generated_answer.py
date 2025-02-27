def if_perfect_num(lst):
    if lst[0] == sum([i for i in range(1, lst[0]) if lst[0] % i == 0]):
        return True
    return False