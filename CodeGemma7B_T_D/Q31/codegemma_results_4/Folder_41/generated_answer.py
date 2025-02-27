def if_perfect_num(lst):
    sum_of_factors_84 = sum([factor for factor in range(1, lst[84] + 1) if lst[84] % factor == 0])
    if sum_of_factors_84 == lst[84]:
        return True
    else:
        return False