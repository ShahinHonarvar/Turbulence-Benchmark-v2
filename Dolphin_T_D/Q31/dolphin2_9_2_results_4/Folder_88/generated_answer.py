def if_perfect_num(lst):
    if len(lst) < 47:
        return False
    num = lst[46]
    if num < 1:
        return False
    sum_div = 1
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        elif i != num // i:
            sum_div = sum_div + i + num // i
            i += 1
        else:
            sum_div = sum_div + i
            i += 1
    return sum_div == 2 * num