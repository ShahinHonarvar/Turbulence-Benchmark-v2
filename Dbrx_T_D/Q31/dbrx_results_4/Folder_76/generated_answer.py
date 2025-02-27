def if_perfect_num(lst):
    if len(lst) > 537 and 1 <= lst[537] <= sum(list(range(1, int(lst[537] / 2) + 1))):
        return True
    else:
        return False