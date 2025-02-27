def if_perfect_num(lst):
    if len(lst) < 22:
        return False
    num = lst[21]
    if num < 1:
        return False
    summa = 1
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        elif i * (num // i) == num:
            summa = summa + i + num // i
            i += 1
        else:
            summa = summa + i
            i += 1
    return summa == num and num != 1