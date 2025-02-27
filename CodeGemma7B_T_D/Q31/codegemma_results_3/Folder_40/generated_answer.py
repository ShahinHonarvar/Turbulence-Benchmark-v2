def if_perfect_num(lst):
    if lst[7] % 2 == 0 or lst[7] % 3 == 0 or lst[7] % 5 == 0 or (lst[7] % 7 == 0):
        return True
    else:
        return False