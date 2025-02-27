def if_perfect_num(num):
    if num[29] == sum(num[:29]):
        return True
    else:
        return False