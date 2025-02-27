def if_perfect_num(lst):
    if len(lst) < 95:
        return False
    num = lst[94]
    sum_factors = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            if i == num // i:
                sum_factors += i
            else:
                sum_factors += i + num // i
    return num == sum_factors