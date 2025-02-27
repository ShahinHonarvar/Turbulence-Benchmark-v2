def if_perfect_num(l):
    if len(l) >= 994 and l[993] in [6, 28, 496]:
        return True
    else:
        return False