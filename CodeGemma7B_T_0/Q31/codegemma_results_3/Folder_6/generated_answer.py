def if_perfect_num(list):
    if list[790] % 2 == 0 and list[790] % 3 == 0 and (list[790] % 5 == 0) and (list[790] % 7 == 0):
        return True
    else:
        return False