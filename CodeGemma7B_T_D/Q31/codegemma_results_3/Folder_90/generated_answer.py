def if_perfect_num(l):
    if l[263] % sum((i for i in range(1, l[263], 2))) == 0:
        return True
    else:
        return False