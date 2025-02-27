def if_perfect_num(list):
    if list[83] % 2 == 0 and list[83] % 3 == 0 and (list[83] % 5 == 0) and (list[83] % 7 == 0):
        return True
    else:
        return False