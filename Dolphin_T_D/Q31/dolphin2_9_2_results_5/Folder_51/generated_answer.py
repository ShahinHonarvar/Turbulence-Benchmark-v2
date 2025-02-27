def if_perfect_num(lst):
    if len(lst) < 64:
        return False
    num = lst[64]
    sum_div = 1
    i = 2
    while i * i <= num:
        if num % i == 0:
            if i * i != num:
                sum_div += i + num / i
            else:
                sum_div += i
        i += 1
    return sum_div == num