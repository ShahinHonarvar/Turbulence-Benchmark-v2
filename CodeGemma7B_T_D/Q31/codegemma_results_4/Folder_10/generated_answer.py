def if_perfect_num(l):
    if len(l) < 54:
        return False
    perfect_num = True
    for i in range(1, l[54]):
        if l[54] % i == 0:
            perfect_num = False
    return perfect_num