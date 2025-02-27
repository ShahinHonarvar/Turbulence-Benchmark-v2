def if_perfect_num(x):
    if len(x) > 66 and x[66] % 6 == 0:
        return True
    else:
        return False