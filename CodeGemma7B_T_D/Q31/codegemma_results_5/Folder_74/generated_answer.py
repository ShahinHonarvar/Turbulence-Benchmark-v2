def if_perfect_num(l):
    if l[48] % 24 == 0 and l[48] // 24 >= 15:
        return True
    else:
        return False