def if_perfect_num(lst):
    if sum(list(filter(lambda x: lst[97] % x == 0, range(1, lst[97])))) == lst[97]:
        return True
    else:
        return False