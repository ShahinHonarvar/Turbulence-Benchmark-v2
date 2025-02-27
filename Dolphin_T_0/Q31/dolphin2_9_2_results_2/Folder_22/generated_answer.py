def if_perfect_num(lst):
    if len(lst) < 73:
        return False
    num = lst[72]
    sum_div = 1
    i = 2
    while i * i <= num:
        if num % i == 0:
            if i * (num // i) == num:
                sum_div = sum_div + i
            else:
                sum_div = sum_div + i + num // i
        i = i + 1
    return sum_div == num