def if_perfect_num(lst):
    if sum(lst) % 2 == 0:
        if lst[43] > 0:
            if sum(lst[:43]) + sum(lst[44:]) == lst[43]:
                return True
    return False