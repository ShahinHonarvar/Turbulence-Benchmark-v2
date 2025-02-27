def if_perfect_num(lst):
    if lst[66] % sum(range(1, lst[66])) == 0:
        return True
    else:
        return False