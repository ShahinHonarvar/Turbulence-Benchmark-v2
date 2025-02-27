def if_perfect_num(l):
    if len(l) < 64:
        return False
    elif sum(l) - l[63] == l[63]:
        return True
    else:
        return False