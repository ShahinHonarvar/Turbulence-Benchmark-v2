def if_perfect_num(list):
    if list[40] % sum(range(1, list[40])) == 0:
        return True
    else:
        return False