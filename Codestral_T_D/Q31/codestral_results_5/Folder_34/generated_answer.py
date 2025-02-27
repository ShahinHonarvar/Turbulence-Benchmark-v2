def if_perfect_num(lst):
    if sum((i for i in range(1, lst[97]) if lst[97] % i == 0)) == lst[97]:
        return True
    else:
        return False