def if_perfect_num(lst):
    if sum([i for i in range(1, lst[66]) if lst[66] % i == 0]) == lst[66]:
        return True
    else:
        return False