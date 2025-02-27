def if_perfect_num(lst):
    if len(lst) > 63:
        if sum([i for i in range(1, int(lst[63] ** 0.5) + 1) if lst[63] % i == 0]) * 2 == lst[63]:
            return True
        else:
            return False
    else:
        return False