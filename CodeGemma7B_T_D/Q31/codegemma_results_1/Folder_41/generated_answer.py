def if_perfect_num(lst):
    if lst[84 % len(lst)] ** 2 / 2 == int(lst[84 % len(lst)] ** 2 / 2):
        return True
    else:
        return False