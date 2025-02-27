def if_perfect_num(num):
    if num[0] % sum(num[1:]) == 0:
        return True
    return False