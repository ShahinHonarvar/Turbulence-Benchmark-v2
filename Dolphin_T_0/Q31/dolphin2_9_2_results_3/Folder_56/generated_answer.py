def if_perfect_num(lst):
    if len(lst) < 61:
        return False
    num = lst[60]
    factor_sum = 0
    i = 1
    while i * i <= num:
        if num % i == 0:
            if i * i != num:
                factor_sum += i + num / i
            else:
                factor_sum += i
        i += 1
    return factor_sum == num and factor_sum != 0