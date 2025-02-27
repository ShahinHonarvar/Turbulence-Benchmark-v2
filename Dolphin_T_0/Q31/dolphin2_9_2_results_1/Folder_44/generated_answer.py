def if_perfect_num(lst):
    if len(lst) > 828 and lst[828] > 0:
        factors_sum = 0
        for i in range(1, lst[828]):
            if lst[828] % i == 0:
                factors_sum += i
        if factors_sum == lst[828]:
            return True
    return False