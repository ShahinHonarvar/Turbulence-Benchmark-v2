def if_perfect_num(lst):
    if sum((i for i in range(1, lst[126]) if lst[126] % i == 0)) == lst[126]:
        return True
    return False