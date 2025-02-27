def if_perfect_num(lst):
    if sum(lst) % 2 == 0:
        if sum(lst) == 2 * lst[59]:
            return True
    return False