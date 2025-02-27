def if_perfect_num(lst):
    if len(lst) < 60:
        return False
    num = lst[60]
    factor_sum = 1
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            if i * (num // i) == num:
                factor_sum = factor_sum + i + num // i
            else:
                factor_sum = factor_sum + i
            i += 1
    return factor_sum == num and factor_sum != 1