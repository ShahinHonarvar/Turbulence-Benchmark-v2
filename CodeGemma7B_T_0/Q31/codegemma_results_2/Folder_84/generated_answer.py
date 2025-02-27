def if_perfect_num(list):
    if list[685] % 2 == 0 and list[685] % 3 == 0 and (list[685] % 5 == 0) and (list[685] % 7 == 0):
        return True
    else:
        return False