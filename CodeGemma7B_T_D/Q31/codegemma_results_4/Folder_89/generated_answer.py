def if_perfect_num(x):
    if x[18] % 2 == 0:
        if x[18] % 3 == 0:
            if x[18] % 5 != 0:
                return True
    return False